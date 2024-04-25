import os  
from dotenv import load_dotenv
from app import connection_string
from sqlalchemy import create_engine
from sqlalchemy import inspect
import json
import pyodbc

print("Connecting to database...")
conn_string = 'mssql+pyodbc:///?odbc_connect=' + connection_string

print("Creating engine...")
engine = create_engine(conn_string)

print("Inspecting database...")
inspector = inspect(engine)

print("Getting table names...")
all_metadata = inspect(engine)
for table_name in inspector.get_table_names():
    table_metadata = inspector.get_columns(table_name)
    all_metadata[table_name] = table_metadata
        
print("Writing metadata to file...")
with open("database_metadata.json", "w") as file:
    json.dump(all_metadata, file, ident=2)
