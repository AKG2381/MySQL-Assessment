"""
1. SQLite
SQLite is a lightweight, file-based database.
"""
# a) Using sqlite3 (Standard Library)
import sqlite3

conn = sqlite3.connect("example.db")  # Connect to the database file
cursor = conn.cursor()
cursor.execute("SELECT sqlite_version();")
print("SQLite version:", cursor.fetchone())
conn.close()


# b) Using SQLAlchemy
from sqlalchemy import create_engine

engine = create_engine("sqlite:///example.db")
with engine.connect() as connection:
    result = connection.execute("SELECT sqlite_version();")
    print("SQLite version:", result.fetchone())



"""
2. MySQL
MySQL is a widely-used relational database.
"""
# a) Using mysql-connector-python
python
Copy code
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()
cursor.execute("SELECT VERSION();")
print("MySQL version:", cursor.fetchone())
conn.close()


#  b) Using pymysql

import pymysql

conn = pymysql.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()
cursor.execute("SELECT VERSION();")
print("MySQL version:", cursor.fetchone())
conn.close()

#  c) Using SQLAlchemy

from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://your_username:your_password@localhost:port/your_database")
with engine.connect() as connection:
    result = connection.execute("SELECT VERSION();")
    print("MySQL version:", result.fetchone())

"""
3. PostgreSQL
PostgreSQL is a robust, open-source relational database.
"""
#  a) Using psycopg2

import psycopg2

conn = psycopg2.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)
cursor = conn.cursor()
cursor.execute("SELECT version();")
print("PostgreSQL version:", cursor.fetchone())
conn.close()

#  b) Using pg8000

import pg8000

conn = pg8000.connect(
    user="your_username",
    password="your_password",
    host="localhost",
    database="your_database"
)
cursor = conn.cursor()
cursor.execute("SELECT version();")
print("PostgreSQL version:", cursor.fetchone())
conn.close()

#  c) Using SQLAlchemy
from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://your_username:your_password@localhost:port/your_database")
with engine.connect() as connection:
    result = connection.execute("SELECT version();")
    print("PostgreSQL version:", result.fetchone())

"""
4. Microsoft SQL Server
Microsoft SQL Server is a popular enterprise-grade database.
"""
#  a) Using pyodbc

import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=your_database;"
    "UID=your_username;"
    "PWD=your_password"
)
cursor = conn.cursor()
cursor.execute("SELECT @@VERSION;")
print("SQL Server version:", cursor.fetchone())
conn.close()


#  b) Using SQLAlchemy

from sqlalchemy import create_engine

engine = create_engine("mssql+pyodbc://your_username:your_password@localhost:port/your_database?driver=ODBC+Driver+17+for+SQL+Server")
with engine.connect() as connection:
    result = connection.execute("SELECT @@VERSION;")
    print("SQL Server version:", result.fetchone())

"""
5. Oracle
Oracle is a commercial database system used in large-scale applications.
"""
#  a) Using cx_Oracle

import cx_Oracle

conn = cx_Oracle.connect(
    "your_username/your_password@localhost:1521/your_service_name"
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM v$version;")
print("Oracle version:", cursor.fetchone())
conn.close()


#  b) Using SQLAlchemy

from sqlalchemy import create_engine
engine = create_engine("oracle+cx_oracle://your_username:your_password@localhost:1521/your_service_name")
with engine.connect() as connection:
    result = connection.execute("SELECT * FROM v$version")
    print("Oracle version:", result.fetchone())
