import pyodbc
import openai
from openai import OpenAI
import os
from app import connection_string
from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain_community.chat_models import ChatOpenAI
from langchain.sql_database import SQLDatabase
from langchain.prompts.chat import ChatPromptTemplate
from sqlalchemy import create_engine


# Establishes the client with OpenAI API key from .env
#client = openai.OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# Establish a connection to the Azure SQL Database
db_engine = create_engine(connection_string)
db = SQLDatabase(db_engine)
print(db.get_tables_names())

db.close()
