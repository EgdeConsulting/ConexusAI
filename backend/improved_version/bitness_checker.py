import struct
import pyodbc
from app import *


# Get Python bitness
python_bitness = struct.calcsize("P") * 8
print(f"Python Bitness: {python_bitness}-bit")
conn_string = 'mssql+pyodbc:///?odbc_connect=' + connection_string
# Connect to the ODBC driver
conn = pyodbc.connect(conn_string)

# Get ODBC driver bitness
driver_bitness = conn.getinfo(pyodbc.SQL_DRIVER_ODBC_VER).split()[3]
print(f"ODBC Driver Bitness: {driver_bitness}-bit")

conn.close()