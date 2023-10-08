import sqlite3

# will create a db if it does not exist
# conn=sqlite3.connect('customer.db')

# create a cursor
# c=conn.cursor()

# # Create a Table
# c.execute("""
# create table customers(
#     first_name text,
#     last_name text,
#     email text
# )

# """
# )

# # Insert rows
# c.execute("""
#     insert into customers values
#     ('Tim','Gonzales','tim@udemy.com')
# """)

# # View the rows - rowid is created in background as a primary key with autonumbered
# c.execute("""
#     select rowid,* from customers
# """)
# c.fetchone()
# c.fetchmany(3)

# Update rows
# c.execute("""
    # update customers set first_name="Mary"
#     where rowid=4
# """)

#Delete records
# c.execute("""
#     delete from customers where rowid=2
# """)

# #Drop Table
# c.execute("""
#     drop table customers
# """)

#function to ad new record in table
def add_one(first,last,email):
    conn=sqlite3.connect('customer.db')
    c=conn.cursor()
    c.execute("""
        insert into customers values (?,?,?)
    """
    ,(first,last,email)
    )
    conn.commit()
    conn.close()
add_one('john','white','asdf@asdf.acom')
# print(c.fetchall()) #will come out as a list of tuples, one row is one tuple

#commit the sql and close
# conn.commit()
# conn.close()
"""
only active responses to be considered
CREATE TABLE fact (
  app_id int, 
  finding_id int, 
  finding_text text
  response_id int, 
  response_text text,
  finding_status text,
  record_update_status text //new,update...

  PRIMARY KEY (app_id, finding_id)
);

CREATE TABLE jira (
  app_id int, 
  jira_id text
  jira_status text

  PRIMARY KEY (app_id, jira_id)
);
Follow upsert logic of Donohoe
https://stackoverflow.com/questions/15277373/sqlite-upsert-update-or-insert

"""