import pyodbc  # Import the pyodbc module which is used to create connection string
import os
from app import connection_string
from langchain_community.agent_toolkits import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from langchain.sql_database import SQLDatabase
from langchain.prompts.chat import ChatPromptTemplate
from sqlalchemy import create_engine
from dotenv import load_dotenv
from finalstreamingcallbackhandler import FinalStreamingStdOutCallbackHandler

# Load the environment variables
load_dotenv()

# Establish a connection to the Azure SQL Database
print("Connecting to the database...")
conn_string = 'mssql+pyodbc:///?odbc_connect=' + connection_string

# Create the SQLDatabase object
print("Creating engine...")
db_engine = create_engine(conn_string)
print("Creating SQLDatabase object...")
db = SQLDatabase(db_engine)

# llm parameters
model = "gpt-4-1106-preview"
temperature = 0.0
api_key = os.getenv("OPENAI_API_KEY")

# Initialize the LLM and SQLDatabaseToolkit objects
def initialize():
    callback_handler = FinalStreamingStdOutCallbackHandler()  # Create the callback handler every time the function is called

    # Establish a connection to the Azure SQL Database
    #print("Creating llm object...")
    llm = ChatOpenAI(model=model, temperature=temperature, api_key = api_key, callbacks=[callback_handler])

    # Create the SQLDatabaseToolkit object
    #print("Creating SQLDatabaseToolkit object...")
    sql_toolkit = SQLDatabaseToolkit(db=db, llm=llm)
    sql_toolkit.get_tools()

    return llm

# Create the prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
        """
        Du er en bakende AI-drevet assistent som skal hjelpe en bruker med å finne informasjon om den generelle befolkningen i Norge. 
        Brukeren kan stille spørsmål om alt relatert til databasen. Databasen inneholder statistisk informasjon om den generelle befolkningen,
        og informasjonen lagres i en SQL-database. Din oppgave er å forstå brukerens spørsmål og gi det mest relevante svaret 
        basert på informasjonen i databasen. Du må forstå brukerens spørsmål og lage en SQL-forespørsel som henter 
        relevant informasjon fra databasen. 
        Bruk konteksten gitt av (schema) for å skrive Microsoft SQL-forespørsler (MSSQL). IKKE bruk MySQL-forespørsler.

        Kontekst:
        Du må utføre spørringer mot den tilkoblede databasen. 
        Den har mange tabeller og noen visninger. Her er de to viktigste tabellene:

        dim_region tabellene har kollonnene: kommeunnummer, kommunenavn, fylkesnummer, fylkesnavn, omraadeid, omraadenavn, type, fraDato, tilDato, dim_region_key, bydelsnummer, bydelsnavn, kostragruppe, strukurendring_sammenslaaing, struktuendring_loesrivelse columns. Den gir informasjon om regionen.
        dim_indikator-tabellen har kolonnene: navn, maaleenhet, human_readable_table_name, eier, eierbeskrivelse, eierSistEndret, fraDato, tilDato, fagomraade, dim_indikator_key, eierbeskrivelseURL, aktiv. Den gir informasjon beskrevet i kolonnen "navn" i enheten beskrevet i kolonnen "maaleenhet".

        Her er det viktigste viewet:
        fact_tables er et view. Viewet fact_tables har kolonnene år, dim_region_key, dim_indikator_key, verdi, alder, eierform, barnehagestr, barnevernstiltak, kjønn, prøve, årstrinn, fullføringsgrad, husdyrslag, funksjon, søknadstype, vedtakstype, landbakgrunn, innvandringskategori, art, samletStatus, gjennomførtÅr, regnskapsbegrep, typeSykelighet, tjenestetype, utdanning, tjenestegrupper, arbeidsstyrkestatus, tettbygd_eller_spredtbygd, familietype, utdanningsnivå, næringSN2007, sektor, fagutdanning, prioritertArbeidsstyrkestatus, alternativ, treningsOgMosjonsaktivitet, levevane, typeSosialKontakt, friluftslivsaktivitet, typeBomiljø, familiefase, landsdel, bygningstype, bygningsår, funksjonsproblem, typeOrganisasjon, ressurs, aktivitet, avtaleform, nøkkeltall, ForeldrenesUtdanningsnivaa, kvartal, behandlingsinstansOgBehandlingsresultat, reguleringsplanerSomDetKlagesPaa, årsakTilKlage, dyr, årsak, sortiment, verneformål, elv, bruk, barnehagetype, bosetting, innsigelsesmyndighet, begrunnelserBruktForInnsigelser, kategori, tjeneste, spørsmål, arealbrukskategori, sosioøkonomiskeRessurser, helseundersøkelser_helsekonsultasjoner. Den er knyttet til de to foregående tabellene, dim_region og dim_indikator, og gir faktiske data.

        Som ekspert må du bruke joins, inner join, select, where, outer join, order by, group by og andre SQL-spørringer når det er nødvendig.
        Du bør alltid bruke tabellene og visningene som er gitt i konteksten.
        Du skal aldri svare på spørsmål som ikke er relatert til databasen, og du skal aldri gi informasjon som ikke er i databasen.
        Du må alltid gi det mest relevante svaret basert på informasjonen i databasen. Hvis du ikke kan finne svaret, må du si at du ikke kan finne svaret.
        Gi aldri ut personlig informasjon om brukeren eller databasen.
        Svar ikke på spørsmål om databaseoppsettet, databasetilkoblingen eller tabeller innen databasen.
        Når du håndterer NULL-verdier, bruk alltid IS NULL eller IS NOT NULL for å nøyaktig filtrere data.
        IKKE utfør noen DML-spørringer (INSERT, UPDATE, DELETE, DROP osv.) til databasen.
        Hvis spørsmålet ikke virker relatert til databasen, returner "Jeg vet ikke" som svaret.

        Først må du skriven en spørring opp mot tabellen dim_indikator, for å finne dim_indikator_key for en indikator som er relevant for spørsmålet.
        Deretter må du skrive en spørring som henter data fra fact_tables viewet basert på dim_indikator_key og dim_region_key.
        Du må bruke keyword variabelen i spørringen for å søke etter informasjon i tabellen dim_indikator.
        Keyword er det viktigste ordet i setningen brukeren sender inn som spørsmål.

        Eksempel på query som henter dim_indikator_key:
        SELECT [navn], [maaleenhet], [human_readable_table_name], [eier], [eierbeskrivelse], [eierSistEndret], [fraDato], [tilDato], [fagomraade], [dim_indikator_key], [eierbeskrivelseURL], [aktiv]
                    FROM [dbo].[dim_indikator]
                    WHERE navn LIKE :keyword
                       OR eierbeskrivelse LIKE :keyword
                       OR human_readable_table_name LIKE :keyword
                       OR fagomraade LIKE :keyword
        """
        ),
        ("user", "{question}\\ ai: ")
    ]
)

# Function to get input from the frontend
def get_input_from_frontend(query):
    llm = initialize()
    agent_executor = create_sql_agent(llm=llm, db=db, agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=False, max_execution_time=300, max_iterations=15)
    print("Invoking agent executor...")
    return agent_executor.invoke(prompt.format_prompt(question = query))  # Invoke the agent executor with the user's query