import os
from dotenv import load_dotenv
import pymssql

# Last inn miljøvariabler
load_dotenv()

user=os.getenv('USERNAME_DB'),
password=os.getenv('PASSWORD_DB'),
database=os.getenv('DATABASE_DB')
# Opprett databaseforbindelse
def get_db_connection():
    return pymssql.connect(server=os.getenv('SERVER_DB'),
                           user=os.getenv('USERNAME_DB'),
                           password=os.getenv('PASSWORD_DB'),
                           database=os.getenv('DATABASE_DB'))

def close_db_connection(conn):
    conn.close()
