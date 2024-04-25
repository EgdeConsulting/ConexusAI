import os  
from dotenv import load_dotenv
from app import connection_string
from sqlalchemy import create_engine
from sqlalchemy import MetaData
import pyodbc
conn_string = 'mssql+pyodbc:///?odbc_connect=' + connection_string

engine = create_engine(conn_string)

metaData = MetaData()

metaData.reflect(bind=engine)

print(metaData.tables.keys())