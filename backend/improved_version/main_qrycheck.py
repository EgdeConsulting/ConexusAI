import os
from dotenv import load_dotenv
from app import connection_string
from langchain_community.utilities import SQLDatabase
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import ChatOpenAI
from langchain_community.tools.sql_database.tool import QuerySQLCheckerTool
import pyodbc

# Load the environment variables
load_dotenv()

print("Establishing a connection to Azure SQL Database...")

# Establish a connection to the Azure SQL Database
conn_string = 'mssql+pyodbc:///?odbc_connect=' + connection_string
api_key = os.getenv("OPENAI_API_KEY")
db_uri = conn_string
db = SQLDatabase.from_uri(db_uri)

# Open the schema file til variable db_schema
#db_schema = open("schema_db.txt", "r")

print("db_schema___:")

# Initialize the OpenAI language model
llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0.0, api_key = api_key)

# Initialize the SQL checker tool
sql_checker = QuerySQLCheckerTool(db=db, llm=llm)

# Define the SQL query prompt template
query_template = """
You are a backend AI-driven assistant that is going to help a user find information
        about the general public of Norway. The user can ask questions about anything
        related to the database. The database contains statistical information about the 
        general public, and the information is stored in an SQL database. Your job is to
        understand the user's question and provide the most relevant answer based on the
        information in the database. You need to understand the user question
        and create an SQL query that retrieves the relevant information from the database.
        Use the below context to write the Microsoft SQL queries, do NOT use MySQL queries.
    Context:
    you must query against the connected database, it has many tables and some views. Here are the two most important tables:
    dim_region table has columns kommeunnummer, kommunenavn, fylkesnummer, fylkesnavn, omraadeid, omraadenavn, type, fraDato, tilDato, dim_region_key, bydelsnummer, bydelsnavn, kostragruppe, strukurendring_sammenslaaing, struktuendring_loesrivelse columns. It gives the region information.
    dim_indikator table has columns navn, maaleenhet, human_readable_table_name, eier, eierbeskrivelse, eierSistEndret, fraDato, tilDato, fagomraade, dim_indikator_key, eierbeskrivelseURL, aktiv columns. It gives information desribed in "navn" in the unit described in "maaleenhet".       
    Here is the most important view:
    fact_tables is a view. The view fact_tables has columns år, dim_region_key, dim_indikator_key, verdi, alder, eierform, barnehagestr, barnevernstiltak, kjønn, prøve, årstrinn, fullføringsgrad, husdyrslag, funksjon, søknadstype, vedtakstype, landbakgrunn, innvandringskategori, art, samletStatus, gjennomførtÅr, regnskapsbegrep, typeSykelighet, tjenestetype, utdanning, tjenestegrupper, arbeidsstyrkestatus, tettbygd_eller_spredtbygd, familietype, utdanningsnivå, næringSN2007, sektor, fagutdanning, prioritertArbeidsstyrkestatus, alternativ, treningsOgMosjonsaktivitet, levevane, typeSosialKontakt, friluftslivsaktivitet, typeBomiljø, familiefase, landsdel, bygningstype, bygningsår, funksjonsproblem, typeOrganisasjon, ressurs, aktivitet, avtaleform, nøkkeltall, ForeldrenesUtdanningsnivaa, kvartal, behandlingsinstansOgBehandlingsresultat, reguleringsplanerSomDetKlagesPaa, årsakTilKlage, dyr, årsak, sortiment, verneformål, elv, bruk, barnehagetype, bosetting, innsigelsesmyndighet, begrunnelserBruktForInnsigelser, kategori, tjeneste, spørsmål, arealbrukskategori, sosioøkonomiskeRessurser, helseundersøkelser_helsekonsultasjoner. It is linked to the two previous tables, dim_region and dim_indikator, and gives the actual data.
    As an expert you must use joins, inne join, select, where, outer join, order by, group by and other SQL statements whenever required. 
    You should always use the tables and views provided in the context.
    You should NEVER answer questions not related to the database, and you should NEVER provide information that is not in the database.
    You must always provide the most relevant answer based on the information in the database. If you cannot find the answer, you should say that you cannot find the answer.
    Never give out personal information about the user or the database.
    Do not answer questions about the database layout, or the database connection, or tables within the database.
    When dealing with NULL values, always use IS NULL or IS NOT NULL to accurately filter data.
    DO NOT make any DML statements (INSERT, UPDATE, DELETE, DROP etc.) to the database.
    If the question does not seem related to the database, just return "I don't know" as the answer.

The schema for the database is given below:
{schema}

Write ONLY the SQL query and nothing else. Do not wrap the SQL query in any other text, not even backticks.

Question: {question}
SQL Query:
"""

# Define the SQL response prompt template
reply_template = """
Based on the table schema below, question, sql query, and sql response, write a natural language response:
{schema}

Question: {question}
SQL Query: {query}
SQL Response: {response}
"""

# Create the prompt templates
query_prompt = ChatPromptTemplate.from_template(query_template)
prompt_response = ChatPromptTemplate.from_template(reply_template)

def get_schema(_):
    return db.get_table_info()

# Define the SQL query generator chain
sql_chain = (
    RunnablePassthrough.assign(schema=get_schema)
    | query_prompt
    | llm.bind(stop=["\nSQLResult:"])  # Stop generating after the SQL query results
    | StrOutputParser()
)

print("db_schema4:")

#print(sql_chain.invoke({"question": "Hvor mange barn 1-2 år er i barnehage i forhold til antall innbyggere 1-2 år i Agder?"}))

# Function to validate and run the query
def validate_and_run_query(query):

    # Check the query for common mistakes
    checked_query = sql_checker.run(query)
    
    # If the checker tool has rewritten the query, use the new query
    if checked_query != query:
        print("Query was corrected by the SQL checker tool.")
        query = checked_query
    
    # Run the validated query
    return db.run(query)

print("Full_Chain_start:")
full_chain = (
    RunnablePassthrough.assign(query=sql_chain).assign(
    schema = get_schema,
    response = lambda variables: validate_and_run_query(variables["query"])
    )
    | prompt_response
    | llm.bind
    #| StrOutputParser()
)

#testing_query = "Hva er gjennomsnittsalder på barn i barnevernet?"
testing_query = "Hvor mange barn 1-2 år er i barnehage i forhold til antall innbyggere 1-2 år i Agder?"
#testing_query = "Hvor mange kvinner i Norge røyker?"

print("This is the sql_chain.invoke:")
print(sql_chain.invoke({"question": testing_query}))

print("##################################################################")
print("##################################################################")

print("This is the full_chain.invoke:")
print(full_chain.invoke({"question": testing_query}))