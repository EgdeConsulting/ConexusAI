from database_manager import DatabaseWrapper
from templates import query_template, reply_template
from config import Config
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLCheckerTool
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

config = Config()
db = DatabaseWrapper() 
print(isinstance(db, SQLDatabase)) 
llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0.0, api_key=config.openai_api_key)
sql_checker = QuerySQLCheckerTool(db=db, llm=llm)
print(isinstance(sql_checker, RunnablePassthrough), " QUERY sql_checker")
def get_schema():
    # Anta at denne metoden henter skjema informasjon fra din database
    print(" QUERY get_schema method called")
    return db.get_table_info()  

def sql_chain(question, schema):
    """Genererer SQL spørring basert på brukerens spørsmål."""
    print(" QUERY sql_chain method called")
    return query_template.format(question=question, schema=schema)

def validate_and_run_query(query):
    """Validerer og kjører SQL spørring mot databasen."""
    print("QUERY validate_and_run_query method called")
    checked_query = sql_checker.run(query)
    try:
        result = db.run_query(checked_query)
        return result
    except Exception as e:
        print(f"Feil ved kjøring av spørring: {e}")
        return None

def handle_user_query(question):
    """Håndterer brukerens spørsmål og returnerer svaret ved å bruke full_chain."""
    print(" QUERY handle_user_query method called")    
    schema = get_schema()  # Henter skjemainformasjon
    query = sql_chain(question, schema)
    result = validate_and_run_query(query)
    if result:
        response = reply_template.format(schema=schema, question=question, query=query, response=result)
        return response
    else:
        return "Ingen data funnet eller en feil oppstod."

# Eksempel på kjøring
if __name__ == "__main__":
    question = "Hva er antall barnehager i Oslo?"
    print(handle_user_query(question))
