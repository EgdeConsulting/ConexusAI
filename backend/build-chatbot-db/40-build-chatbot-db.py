import os
import pyodbc
from openai import OpenAI
from key import APIkey
from sqlalchemy import create_engine
from sqlalchemy.engine.url import URL
from langchain.sql_database import SQLDatabase
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType

#setting Azure SQL env variables
os.environ["SQL_SERVER_USERNAME"] = "egdeadmin" 
os.environ["SQL_SERVER_ENDPOINT"] = "tcp:datavarehusetdb.database.windows.net,1433"
os.environ["SQL_SERVER_PASSWORD"] = "ConexusAI!"
os.environ["SQL_SERVER_DATABASE"] = "asql-processed-prod-dw-2024-2-13-17-9"


# Define the cnxn connection string
server = 'tcp:datavarehusetdb.database.windows.net,1433'
database = 'asql-processed-prod-dw-2024-2-13-17-9'
username = 'egdeadmin'
password = 'ConexusAI!'
driver = '{ODBC Driver 18 for SQL Server}'
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'


cnxn = pyodbc.connect(connection_string)  
cursor = cnxn.cursor()  
print(cursor.execute("select top 10 * from dbo.[dim_indikator]"))
results = cursor.fetchall()

for row in results:
    print(row)

db_config = {  
    'drivername': 'mssql+pyodbc',  
    'username': os.environ["SQL_SERVER_USERNAME"] + '@' + os.environ["SQL_SERVER_ENDPOINT"],  
    'password': os.environ["SQL_SERVER_PASSWORD"],  
    'host': os.environ["SQL_SERVER_ENDPOINT"],  
    'port': 1433,  
    'database': os.environ["SQL_SERVER_DATABASE"],  
    'query': {'driver': 'ODBC Driver 18 for SQL Server'}  
}  

db_url = URL(**db_config)
db = SQLDatabase.from_uri(db_url)
#db = SQLDatabase.from_uri(connection_string)

"""
from langchain.chat_models import AzureChatOpenAI

#setting Azure OpenAI env variables

os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = "xxx"
os.environ["OPENAI_API_KEY"] = "xxx"

"""

os.environ["OPENAI_API_KEY"] = "APIkey"
os.environ["OPENAI_API_VERSION"] = "2023-03-15-preview"
os.environ["OPENAI_API_BASE"] = "https://api.openai.com"

# Create a new chat model
#llm = OpenAI.ChatModel(deployment_name="gpt-4", temperature=0, max_tokens=4000)
llm = OpenAI.chat(deployment_name="gpt-4", temperature=0, max_tokens=4000)

toolkit = SQLDatabaseToolkit(db=db, llm=llm)

agent_executor = create_engine(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

agent_executor.run("Hvor mange rader er det i tabellen dim_indikator?")