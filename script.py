# run python script through the shell
# sudo sudo -u postgres psql to activate postgresql

# This script creates Table
import psycopg2
conn = psycopg2.connect("host=localhost dbname=branch1 user=postgres password=my_postgres_password")
cur = conn.cursor()
cur.execute("""
    CREATE TABLE Customer(
    custID INTEGER PRIMARY KEY,
    firstName VARCHAR(80) NOT NULL,
    lastName VARCHAR(80) NOT NULL,
    email VARCHAR(80) NOT NULL,
    cellNum VARCHAR(80) NOT NULL)
""")
cur.execute("""
    CREATE TABLE Employee (
        empID VARCHAR(50) PRIMARY KEY,
        empFirstName VARCHAR(80) NOT NULL,
        empLastName VARCHAR(80) NOT NULL,
        empType VARCHAR(80) NOT NULL
    )
""")
cur.execute("""
     CREATE TABLE Branch (
                branchID varchar(80),
                street varchar(80),
                city varchar(80),
                parish varchar(80),
                primary key(branchID)
        )
""")
cur.execute("""
     CREATE TABLE Laptop (
                serialNum varchar(80),
                brand varchar(80),
                model varchar(80),
                primary key(serialNum)
                )
""")
cur.execute("""
     CREATE TABLE Warehouse (
               Wname varchar(80),
               street varchar(80),
               city varchar(80),
               qty INTEGER,
               primary key(Wname)
        )
""")

conn.commit()

# Inserts rows from CSV into database
import psycopg2
conn = psycopg2.connect("host=localhost dbname=branch1 user=postgres password=my_postgres_password")
cur = conn.cursor()
with open('customers.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'customer', sep=',')

conn.commit()

with open('employee.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'employee', sep=',')

conn.commit()

with open('laptops.csv', 'r') as f:
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'laptop', sep=',')

conn.commit()

with open('warehouse.csv', 'r') as f: # extra field names causing an error
    # Notice that we don't need the `csv` module.
    next(f)  # Skip the header row.
    cur.copy_from(f, 'warehouse', sep=',')

conn.commit()