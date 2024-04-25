import os  
from dotenv import load_dotenv
from app import connection_string
from sqlalchemy import create_engine
from sqlalchemy import MetaData
import pyodbc
conn_string = 'mssql+pyodbc:///?odbc_connect=' + connection_string

print("Creating engine...")
engine = create_engine(conn_string)

print("Creating metadata...")
metaData = MetaData()

print("Reflecting metadata...")
metaData.reflect(bind=engine)

#print(metaData.tables.keys())

print("Writing to file...")
try:
    with open("schema_reflect.txt", "w") as file:
        for item in metaData.sorted_tables():
            file.write(item + "\n")
except Exception as e:
    print(e)
    print("Error writing to file")

