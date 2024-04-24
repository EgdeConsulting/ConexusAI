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
 
print("Initializing the llm model...")
 
# Initialize the OpenAI language model
llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0.0, api_key = api_key)
 
# Initialize the SQL checker tool
sql_checker = QuerySQLCheckerTool(db=db, llm=llm)
 
#with open("query_template_norsk.txt", "r") as file:
    #query_template = file.read()
 
# Define the SQL query prompt template
query_template = """
Du er en bakende AI-drevet assistent som skal hjelpe en bruker med å finne informasjon om den generelle befolkningen i Norge.
Brukeren kan stille spørsmål om alt relatert til databasen. Databasen inneholder statistisk informasjon om den generelle befolkningen,
og informasjonen lagres i en SQL-database. Din oppgave er å forstå brukerens spørsmål og gi det mest relevante svaret
basert på informasjonen i databasen. Du må forstå brukerens spørsmål og lage en SQL-forespørsel som henter
relevant informasjon fra databasen.
Bruk den nedenforstående konteksten for å skrive Microsoft SQL-forespørsler; IKKE bruk MySQL-forespørsler.
 
Kontekst:
Du må utføre spørringer mot den tilkoblede databasen.
Den har mange tabeller og noen visninger. Her er de to viktigste tabellene:
 
dim_region tabellene har kollonnene: kommeunnummer, kommunenavn, fylkesnummer, fylkesnavn, omraadeid, omraadenavn, type, fraDato, tilDato, dim_region_key, bydelsnummer, bydelsnavn, kostragruppe, strukurendring_sammenslaaing, struktuendring_loesrivelse columns. Den gir informasjon om regionen.
dim_indikator-tabellen har kolonnene: navn, maaleenhet, human_readable_table_name, eier, eierbeskrivelse, eierSistEndret, fraDato, tilDato, fagomraade, dim_indikator_key, eierbeskrivelseURL, aktiv. Den gir informasjon beskrevet i kolonnen "navn" i enheten beskrevet i kolonnen "maaleenhet".
 
Her er det viktigste viewet:
fact_tables er et view. Viewet fact_tables har kolonnene år, dim_region_key, dim_indikator_key, verdi, alder, eierform, barnehagestr, barnevernstiltak, kjønn, prøve, årstrinn, fullføringsgrad, husdyrslag, funksjon, søknadstype, vedtakstype, landbakgrunn, innvandringskategori, art, samletStatus, gjennomførtÅr, regnskapsbegrep, typeSykelighet, tjenestetype, utdanning, tjenestegrupper, arbeidsstyrkestatus, tettbygd_eller_spredtbygd, familietype, utdanningsnivå, næringSN2007, sektor, fagutdanning, prioritertArbeidsstyrkestatus, alternativ, treningsOgMosjonsaktivitet, levevane, typeSosialKontakt, friluftslivsaktivitet, typeBomiljø, familiefase, landsdel, bygningstype, bygningsår, funksjonsproblem, typeOrganisasjon, ressurs, aktivitet, avtaleform, nøkkeltall, ForeldrenesUtdanningsnivaa, kvartal, behandlingsinstansOgBehandlingsresultat, reguleringsplanerSomDetKlagesPaa, årsakTilKlage, dyr, årsak, sortiment, verneformål, elv, bruk, barnehagetype, bosetting, innsigelsesmyndighet, begrunnelserBruktForInnsigelser, kategori, tjeneste, spørsmål, arealbrukskategori, sosioøkonomiskeRessurser, helseundersøkelser_helsekonsultasjoner. Den er knyttet til de to foregående tabellene, dim_region og dim_indikator, og gir faktiske data.
 
Som ekspert må du bruke joins, inner join, select, where, outer join, order by, group by og andre SQL-uttalelser når det er nødvendig.
Du bør alltid bruke tabellene og visningene som er gitt i konteksten.
Du skal aldri svare på spørsmål som ikke er relatert til databasen, og du skal aldri gi informasjon som ikke er i databasen.
Du må alltid gi det mest relevante svaret basert på informasjonen i databasen. Hvis du ikke kan finne svaret, må du si at du ikke kan finne svaret.
Gi aldri ut personlig informasjon om brukeren eller databasen.
Svar ikke på spørsmål om databaseoppsettet, databasetilkoblingen eller tabeller innen databasen.
Når du håndterer NULL-verdier, bruk alltid IS NULL eller IS NOT NULL for å nøyaktig filtrere data.
IKKE utfør noen DML-uttalelser (INSERT, UPDATE, DELETE, DROP osv.) til databasen.
Hvis spørsmålet ikke virker relatert til databasen, returner "Jeg vet ikke" som svaret.
 
Eksempel på en query fra spørmålet Hvor mange elever er det på alle trinn i Oslo i år 2023?
SELECT *
FROM fact_grunnskole_nokkeltall
JOIN dim_region ON fact_grunnskole_nokkeltall.dim_region_key = dim_region.dim_region_key
WHERE dim_region.kommunenavn = 'Oslo'
AND fact_grunnskole_nokkeltall.år = '2023-24'
 
returnerer dette:
dim_region_key  dim_indikator_key   eierform    verdi   Kjønn   Prøve   år  id  Årstrinn    fullføringsgrad alder   funksjon    ForeldrenesUtdanningsnivaa  kommunenummer   kommunenavn fylkesnummer    fylkesnavn  omraadeid   omraadenavn type    fraDato tilDato dim_region_key  bydelsnummer    bydelsnavn  kostragruppe    strukturendring_sammenslaaing   strukturendring_loesrivelse
2396    144 Privat eiet 20.1    Alle kjønn  Engelsk 2023-24 20657   5. årstrinn NULL    NULL    NULL    NULL    301 Oslo    NULL    NULL    NULL    NULL    Kommune 01/01/1900  31/12/2099  2396    NULL    NULL    1702    NULL    NULL
2396    144 Privat eiet 25.7    Alle kjønn  Regning 2023-24 30105   5. årstrinn NULL    NULL    NULL    NULL    301 Oslo    NULL    NULL    NULL    NULL    Kommune 01/01/1900  31/12/2099  2396    NULL    NULL    1702    NULL    NULL
2396    144 Privat eiet 19.1    Jente   Lesing  2023-24 3327    5. årstrinn NULL    NULL    NULL    NULL    301 Oslo    NULL    NULL    NULL    NULL    Kommune 01/01/1900  31/12/2099  2396    NULL    NULL    1702    NULL    NULL
2396    666 Privat eiet 3   Gutt    Regning 2023-24 12462   9. årstrinn NULL    NULL    NULL    NULL    301 Oslo    NULL    NULL    NULL    NULL    Kommune 01/01/1900  31/12/2099  2396    NULL    NULL    1702    NULL    NULL
2396    144 Offentlig skole 18.6    Alle kjønn  Lesing  2023-24 54263   5. årstrinn NULL    NULL    NULL    NULL    301 Oslo    NULL    NULL    NULL    NULL    Kommune 01/01/1900  31/12/2099  2396    NULL    NULL    1702    NULL    NULL
 
Schema for databasen er gitt nedenfor:
{schema}
 
Returner kun SQL spørringen og ingenting annet. Ikke pakk SQL spørringen i annen tekst, ikke engang backticks.
 
Question: {question}
SQL Query:
"""
 
# Define the SQL response prompt template
reply_template = """
Based on the table schema below, question, sql query, and sql response, write a natural language response:
Basert på tabell schema nedenfor, spørsmål, sql spørring, og sql respons, skriv et naturlig språk svar (natural language resposne) på norsk
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
 
#print(sql_chain.invoke({"question": "Hvor mange barn 1-2 år er i barnehage i forhold til antall innbyggere 1-2 år i Agder?"}))
 
print("Input the validated question to the SQL database...")
 
# Function to validate and run the query
def validate_and_run_query(query):
    for _ in range(2):
        # Check the query for common mistakes
        checked_query = sql_checker.run(query)
        print(f"run number {_}")
        
        # If the checker tool has rewritten the query, use the new query
        if checked_query != query:
            print("Query was corrected by the SQL checker tool.")
            query = checked_query
        
        try:
            # Run the validated query
            result = db.run(query)
            return result
        except Exception as e:
            print(f"Error occurred: {e}")
            # Optionally, you can choose to retry with the original query or stop the loop and return None
            # query = original_query
            # continue
    return None
 
 
print("Full_Chain_start:")
full_chain = (
    RunnablePassthrough.assign(query=sql_chain).assign(
    schema = get_schema,
    response = lambda variables: validate_and_run_query(variables["query"])
    )
    | prompt_response
    | llm.bind(stop=["\nSQLResult:"])
    | StrOutputParser()
)
 
#testing_query = "Hva er gjennomsnittsalder på barn i barnevernet?"
#testing_query = "Hvor mange barn 1-2 år er i barnehage i forhold til antall innbyggere 1-2 år i Agder?"
#testing_query = "Hvor mange kvinner i Norge røyker?"
testing_query = "Hvor mange elever er det på alle trinn i Oslo i år 2023?"
 
print("This is the sql_chain.invoke:")
print(sql_chain.invoke({"question": testing_query}))
 
print("##################################################################")
print("##################################################################")
 
print("This is the full_chain.invoke:")
print(full_chain.invoke({"question": testing_query}))