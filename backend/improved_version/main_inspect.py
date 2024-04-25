import os  
from dotenv import load_dotenv
from app import connection_string
from sqlalchemy import create_engine
from sqlalchemy import inspect
import json
import pyodbc

conn_string = 'mssql+pyodbc:///?odbc_connect=' + connection_string

engine = create_engine(conn_string)

inspector = inspect(engine)

all_metadata = inspect(engine)
for table_name in inspector.get_table_names():
    table_metadata = inspector.get_columns(table_name)
    all_metadata[table_name] = table_metadata
        

with open("database_metadata.json", "w") as file:
    json.dump(all_metadata, file, ident=2)
