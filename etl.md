### ETL Pipeline Overview
Data will be pulled from multiple APIs / files / databases and processed into these zones:
* Staging zone
* Conformed zone
* Semantic zone

All these zones will be built in cockroach db on-prem in GAP in different schemas.

no REST API development required for phase I

### Staging Zone
**Purpose**: Storage area where raw data from different sources are collected.

**Characteristics**:
- Raw, unprocessed data as fetched from sources
- Minimal transformations (e.g., format conversions)
- Short retention period. Data retained for last 3 pulls for traceability

**Steps**:
1. **Extract Data**:
   - Connect to source systems (e.g., databases, APIs, flat files).
   - Extract data using vanilla object oriented python (no frameworks/pandas/petl) primarily using requests module. aiohttp to be used where async needed.
   - Store the data as-is in the staging zone

2. **Format Conversion**:
   - Convert the data into json format as list of arrays.

### Conformed Zone
**Purpose**: Data is standardized and cleaned to ensure consistency across different sources.

**Characteristics**:
- Bulk of the business logic resides in this zone
- Data loaded from staging zone into tables based on OLAP data model
- Business rules applied
- Use SQL DBT models to hold tranformation code
- Implement data validation / data quality checks
- Implement change data capture (CDC) for all data
- 3 year retention period


### Semantic Zone
**Purpose**: Data is refined and optimized for end-user consumption, including reporting and analytics.

**Characteristics**:
- Aggregated and summarized data
- Use SQL DBT model for transformation code
- Optimized for specific use cases (e.g., dashboards, static reports, upload formats to watershed)
- star schema model for Qlik BI tool
- 3 year retention period

**Orchestration**:
- Control M for task orchestration

   
**Logging and Monitoring**:
   - Implement robust logging and monitoring to track ETL process performance and errors.
   
**Testing**:
   - Implement robust testing and minimum of 80% code coverage.
   
**Scalability**:
   - ETL pipeline should handle increasing data volumes and varying load conditions.

**Documentation**:
   - Ensure adequate documentation of logic


### Deployment : 
- Jules deployment

### Version Control : 
- bitbucket

### Data Models required : 
- OLAP data model for conformed zone
- star schema for semantic zone
