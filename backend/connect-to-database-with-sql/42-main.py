import pyodbc
import openai
from openai import OpenAI
import os
from app import connection_string

# Establishes the client with OpenAI API key from .env
client = openai.OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

# Establish a connection to the Azure SQL Database
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Execute the SELECT query
#cursor.execute('SELECT * FROM fact_barnehage_nokkeltall')

# Fetch and print the results
for row in cursor.fetchall():
    print(row)

from string import Template

t = Template("""
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
    dim_region table has kommeunnummer, kommunenavn, fylkesnummer, fylkesnavn, omraadeid, omraadenavn, type, fraDato, tilDato, dim_region_key, bydelsnummer, bydelsnavn, kostragruppe, strukurendring_sammenslaaing, struktuendring_loesrivelse columns. It gives the region information.
    dim_indikator table has navn, maaleenhet, human_readable_table_name, eier, eierbeskrivelse, eierSistEndret, fraDato, tilDato, fagomraade, dim_indikator_key, eierbeskrivelseURL, aktiv columns. It gives information desribed in "navn" in the unit described in "maaleenhet".       
    the view fact_tables has år, dim_region_key, dim_indikator_key, verdi, alder, eierform, barnehagestr, barnevernstiltak, kjønn, prøve, årstrinn, fullføringsgrad, husdyrslag, funksjon, søknadstype, vedtakstype, landbakgrunn, innvandringskategori, art, samletStatus, gjennomførtÅr, regnskapsbegrep, typeSykelighet, tjenestetype, utdanning, tjenestegrupper, arbeidsstyrkestatus, tettbygd_eller_spredtbygd, familietype, utdanningsnivå, næringSN2007, sektor, fagutdanning, prioritertArbeidsstyrkestatus, alternativ, treningsOgMosjonsaktivitet, levevane, typeSosialKontakt, friluftslivsaktivitet, typeBomiljø, familiefase, landsdel, bygningstype, bygningsår, funksjonsproblem, typeOrganisasjon, ressurs, aktivitet, avtaleform, nøkkeltall, ForeldrenesUtdanningsnivaa, kvartal, behandlingsinstansOgBehandlingsresultat, reguleringsplanerSomDetKlagesPaa, årsakTilKlage, dyr, årsak, sortiment, verneformål, elv, bruk, barnehagetype, bosetting, innsigelsesmyndighet, begrunnelserBruktForInnsigelser, kategori, tjeneste, spørsmål, arealbrukskategori, sosioøkonomiskeRessurser, helseundersøkelser_helsekonsultasjoner. It is linked to the two previous tables, dim_region and dim_indikator, and gives the actual data.
    As an expert you must use joins whenever required.


===========
$options
===========
""")

sorted_result = []

system_prompt = t.substitute(options = "\n\n".join([item[0] for item in sorted_result[:3]]))
print(system_prompt)

# Ask a question using OpenAI's API
user_query = "Hvor mange barnehager er det i Norge?"

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_query,
        }
    ],
    model="gpt-4",
)

# Extract the response from OpenAI
answer = chat_completion.choices[0].message.content

# Execute a generic query to search the entire database
query = f"SELECT * FROM asql-processed-prod-dw-2024-2-13-17-9 WHERE question LIKE {answer}"
cursor.execute(query)

# Fetch and print the results
for row in cursor.fetchall():
    print(row)


# Close the cursor and connection
cursor.close()
conn.close()