import sqlite3
from sqlite3 import Error

def sql_connection():
    try:
        con=sqlite3.connect('mydatabase.db')
        return con
    except Error:
        print(Error)

