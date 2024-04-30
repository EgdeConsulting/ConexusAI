import os
from dotenv import load_dotenv

load_dotenv()

# Define the connection string
server = os.getenv('server')
database = os.getenv('database')
username = os.getenv('login')

password = os.getenv('password')
driver = os.getenv('driver')


connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'