```python
import re
from typing import Dict, List, Any
from datetime import datetime
from loguru import logger

class DatabaseMigrator:
    """Migrates tables and data from source to target MySQL database, preserving PK/FK integrity."""

    def __init__(
        self,
        source_db_config: Dict,
        target_db_config: Dict,
        source_schema: str,
        target_schema: str,
        batch_size: int = 50,
    ):
        self.source = DBClient(db_name=source_schema, config=source_db_config)
        self.target = DBClient(db_name=target_schema, config=target_db_config)
        self.source_schema = source_schema
        self.target_schema = target_schema
        self.batch_size = batch_size
        self.record_date = datetime.now().strftime("%Y-%m-%d")

    def migrate(self):
        logger.info("Starting migration process")
        self.drop_target_tables()
        tables = self.get_source_tables()
        fk_info = self.get_foreign_keys()
        self.create_tables_with_original_ddl(tables)
        self.create_foreign_keys(fk_info)
        ordered_tables = self.topological_sort_tables(tables, fk_info)
        self.copy_data(ordered_tables)
        self.sync_auto_increment(tables)
        logger.info("Migration completed successfully")

    def drop_target_tables(self):
        logger.info("Dropping all tables in target schema")
        tables = self.target.get_all_tables(self.target_schema)
        self.target.data_updater.execute_query("SET FOREIGN_KEY_CHECKS = 0")
        for table in tables:
            self.target.drop_table(table)
        self.target.data_updater.execute_query("SET FOREIGN_KEY_CHECKS = 1")

    def get_source_tables(self) -> List[str]:
        return self.source.get_all_tables(self.source_schema)

    def get_foreign_keys(self) -> List[Dict[str, Any]]:
        query = f"""
            SELECT
                CONSTRAINT_NAME, TABLE_NAME, COLUMN_NAME,
                REFERENCED_TABLE_NAME, REFERENCED_COLUMN_NAME,
                UPDATE_RULE, DELETE_RULE
            FROM information_schema.KEY_COLUMN_USAGE
            WHERE TABLE_SCHEMA = '{self.source_schema}'
              AND REFERENCED_TABLE_NAME IS NOT NULL
            ORDER BY TABLE_NAME, CONSTRAINT_NAME
        """
        return self.source.query_from_db(query)

    def create_tables_with_original_ddl(self, tables: List[str]):
        logger.info("Creating tables in target using original DDL")
        for table in tables:
            ddl_result = self.source.query_from_db(f"SHOW CREATE TABLE {table}")
            if not ddl_result:
                logger.warning(f"No DDL found for table {table}")
                continue
            ddl = ddl_result[0]["Create Table"]
            ddl = self._clean_ddl(ddl)
            self.target.data_updater.execute_query(ddl)

    def _clean_ddl(self, ddl: str) -> str:
        # Remove AUTO_INCREMENT values for idempotency
        return re.sub(r"AUTO_INCREMENT=\d+\s*", "", ddl)

    def create_foreign_keys(self, fk_info: List[Dict[str, Any]]):
        logger.info("Creating foreign key constraints in target")
        grouped = self._group_foreign_keys(fk_info)
        for constraint_name, info in grouped.items():
            stmt = (
                f"ALTER TABLE {info['table']} ADD CONSTRAINT {constraint_name} "
                f"FOREIGN KEY ({', '.join(info['columns'])}) "
                f"REFERENCES {info['ref_table']}({', '.join(info['ref_columns'])})"
            )
            if info['update_rule'] and info['update_rule'] != "RESTRICT":
                stmt += f" ON UPDATE {info['update_rule']}"
            if info['delete_rule'] and info['delete_rule'] != "RESTRICT":
                stmt += f" ON DELETE {info['delete_rule']}"
            try:
                self.target.data_updater.execute_query(stmt)
            except Exception as e:
                logger.warning(f"Could not create FK {constraint_name}: {e}")

    def _group_foreign_keys(self, fk_info: List[Dict[str, Any]]) -> Dict[str, Dict]:
        grouped = {}
        for fk in fk_info:
            name = fk["CONSTRAINT_NAME"]
            if name not in grouped:
                grouped[name] = {
                    "table": fk["TABLE_NAME"],
                    "columns": [],
                    "ref_table": fk["REFERENCED_TABLE_NAME"],
                    "ref_columns": [],
                    "update_rule": fk["UPDATE_RULE"],
                    "delete_rule": fk["DELETE_RULE"],
                }
            grouped[name]["columns"].append(fk["COLUMN_NAME"])
            grouped[name]["ref_columns"].append(fk["REFERENCED_COLUMN_NAME"])
        return grouped

    def topological_sort_tables(self, tables: List[str], fk_info: List[Dict[str, Any]]) -> List[str]:
        # Build dependency graph
        deps = {table: set() for table in tables}
        for fk in fk_info:
            deps[fk["TABLE_NAME"]].add(fk["REFERENCED_TABLE_NAME"])
        ordered = []
        visited = set()
        def visit(table):
            if table in visited:
                return
            for dep in deps[table]:
                visit(dep)
            visited.add(table)
            ordered.append(table)
        for table in tables:
            visit(table)
        return ordered

    def copy_data(self, ordered_tables: List[str]):
        logger.info("Copying data from source to target")
        for table in ordered_tables:
            query = f"SELECT * FROM {table} LIMIT {self.batch_size}"
            records = self.source.query_from_db(query)
            if not records:
                continue
            self.target.data_updater.execute_query("SET @@session.sql_mode = 'NO_AUTO_VALUE_ON_ZERO'")
            self.target.write_to_db(
                records_to_insert=records,
                table_name=table,
                record_date=self.record_date,
                rows_to_commit=self.batch_size,
                update_with_mandatory_columns=False  # preserve original PK/FK
            )
            self.target.data_updater.execute_query("SET @@session.sql_mode = ''")

    def sync_auto_increment(self, tables: List[str]):
        logger.info("Syncing AUTO_INCREMENT values in target")
        for table in tables:
            query = f"""
                SELECT AUTO_INCREMENT FROM information_schema.TABLES
                WHERE TABLE_SCHEMA = '{self.source_schema}' AND TABLE_NAME = '{table}'
            """
            result = self.source.query_from_db(query)
            if result and result[0].get("AUTO_INCREMENT"):
                next_value = result[0]["AUTO_INCREMENT"]
                stmt = f"ALTER TABLE {table} AUTO_INCREMENT = {next_value}"
                self.target.data_updater.execute_query(stmt)

# Usage Example
def main():
    source_config = {
        "dev": {"host": "source-host", "port": 3306}
    }
    target_config = {
        "dev": {"host": "target-host", "port": 3306}
    }
    migrator = DatabaseMigrator(
        source_db_config=source_config,
        target_db_config=target_config,
        source_schema="source_db",
        target_schema="target_db"
    )
    migrator.migrate()

if __name__ == "__main__":
    main()
```