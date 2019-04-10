#!/usr/bin/python
 
import psycopg2
#from config import config

"""
        CREATE TABLE CreditCard (
                cctype varchar(80),
                ccNum varchar(80),
                expDate date,
                CCV varchar(80),
                primary key(ccytype)
        )
        """
 
def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        """
        CREATE TABLE Customer (
             custID INTEGER PRIMARY KEY,
             firstName VARCHAR(80) NOT NULL,
             lastName VARCHAR(80) NOT NULL,
             email VARCHAR(80) NOT NULL,
             cellNum VARCHAR(80) NOT NULL)
        )
        """,
        """ CREATE TABLE Employee (
                empID INTEGER PRIMARY KEY,
                empFirstName VARCHAR(80) NOT NULL,
                empLastName VARCHAR(80) NOT NULL,
                empType VARCHAR(80) NOT NULL
                )
        """,
        """
        CREATE TABLE Branch (
                branchID varchar(80),
                street varchar(80),
                city varchar(80),
                parish varchar(80),
                primary key(branchID)
        )
        """,
        """ CREATE TABLE Laptop (
                serialNum varchar(80),
                brand varchar(80),
                model varchar(80),
                primary key(serialNum)
                )
        """,
        """
        CREATE TABLE CreditCard (
                serialNum varchar(80),
                brand varchar(80),
                model varchar(80),
                primary key(serialNum)
        )
        """,
        """
        CREATE TABLE Warehouse (
               Wname varchar(80),
               street varchar(80),
               city varchar(80),
               qty INTEGER,
               primary key(Wname)
        )
        """)
    conn = None
    try:
        # read the connection parameters
        #params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect("host=localhost dbname=branch1 user=postgres password=my_postgres_password")
        #conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
 
 
if __name__ == '__main__':
    create_tables()