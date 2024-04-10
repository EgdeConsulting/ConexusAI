import pyodbc
import openai
from openai import OpenAI
import os
from app import connection_string
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain.agents import AgentExecutor
from langchain_openai import ChatOpenAI
from langchain.sql_database import SQLDatabase
from langchain.prompts.chat import ChatPromptTemplate
from sqlalchemy import create_engine, inspect
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()

# Establish a connection to the Azure SQL Database
conn_string = 'mssql+pyodbc:///?odbc_connect=' + connection_string
db_engine = create_engine(conn_string)
db = SQLDatabase(db_engine)

#inspection = inspect(db_engine)
#print(inspection.get_table_names()) #confirmed, works!

# Establish a connection to the Azure SQL Database
llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0.0, api_key = os.getenv("OPENAI_API_KEY"))

sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)
sql_toolkit.get_tools()

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
        """
        You are a backend AI-driven assistant that is going to help a user find information
        about the general public of Norway. The user can ask questions about anything
        related to the database. The database contains statistical information about the 
        general public, and the information is stored in an SQL database. Your job is to
        understand the user's question and provide the most relevant answer based on the
        information in the database. You need to understand the user question
        and create an SQL query that retrieves the relevant information from the database.
        Use the below context to write the Microsoft SQL queries, do NOT use MySQL queries.
    Context:
    you must query against the connected database, it has many tables and some views, but these are the important ones:
    dim_region table has columns kommeunnummer, kommunenavn, fylkesnummer, fylkesnavn, omraadeid, omraadenavn, type, fraDato, tilDato, dim_region_key, bydelsnummer, bydelsnavn, kostragruppe, strukurendring_sammenslaaing, struktuendring_loesrivelse columns. It gives the region information.
    dim_indikator table has columns navn, maaleenhet, human_readable_table_name, eier, eierbeskrivelse, eierSistEndret, fraDato, tilDato, fagomraade, dim_indikator_key, eierbeskrivelseURL, aktiv columns. It gives information desribed in "navn" in the unit described in "maaleenhet".       
    fact_tables is a view. The view fact_tables has columns år, dim_region_key, dim_indikator_key, verdi, alder, eierform, barnehagestr, barnevernstiltak, kjønn, prøve, årstrinn, fullføringsgrad, husdyrslag, funksjon, søknadstype, vedtakstype, landbakgrunn, innvandringskategori, art, samletStatus, gjennomførtÅr, regnskapsbegrep, typeSykelighet, tjenestetype, utdanning, tjenestegrupper, arbeidsstyrkestatus, tettbygd_eller_spredtbygd, familietype, utdanningsnivå, næringSN2007, sektor, fagutdanning, prioritertArbeidsstyrkestatus, alternativ, treningsOgMosjonsaktivitet, levevane, typeSosialKontakt, friluftslivsaktivitet, typeBomiljø, familiefase, landsdel, bygningstype, bygningsår, funksjonsproblem, typeOrganisasjon, ressurs, aktivitet, avtaleform, nøkkeltall, ForeldrenesUtdanningsnivaa, kvartal, behandlingsinstansOgBehandlingsresultat, reguleringsplanerSomDetKlagesPaa, årsakTilKlage, dyr, årsak, sortiment, verneformål, elv, bruk, barnehagetype, bosetting, innsigelsesmyndighet, begrunnelserBruktForInnsigelser, kategori, tjeneste, spørsmål, arealbrukskategori, sosioøkonomiskeRessurser, helseundersøkelser_helsekonsultasjoner. It is linked to the two previous tables, dim_region and dim_indikator, and gives the actual data.
    As an expert you must use joins whenever required. You are NEVER allowed to delete or drop a table.
        """
        ),
        ("user", "{question}\ ai: ")
    ]
)
agent_executor = create_sql_agent(llm=llm, db=db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose = True, max_execution_time = 100, max_iterations = 1000)
#agent_executor.invoke(
    #"Hvor mange barnehager er det i Norge?"
#)


# Queries to test with agent
#user_query = "Hvor mange menn røyker?"
#user_query = "Hvor mange barn 1-2 år er i barnehage i forhold til innbyggere 1-2 år i Agder?" #svar = 82.5%
#user_query = "Hvor mange barn 1-2 år er i barnehage i forhold til innbyggere 1-2 år i Agder i år 2023?" #år 2023 er bait, er ikke med i datasettet
user_query = "Hvor mange barn 1-2 år er i barnehage i forhold til innbyggere 1-2 år i Agder i år 2020?" # answer = 81%

agent_executor.invoke(prompt.format_prompt(question = user_query))

def api_query(user_query):
    return agent_executor.invoke(prompt.format_prompt(question = user_query))