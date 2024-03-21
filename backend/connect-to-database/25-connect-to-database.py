from app import connection_string
import pyodbc
import openai
from openai import OpenAI
from key import APIkey

# OpenAI API key
client = OpenAI(api_key = APIkey)

# Establish a connection to the Azure SQL Database
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

"""
# Execute the SELECT query
cursor.execute('SELECT * FROM fact_barnehage_nokkeltall')

# Fetch and print the results
for row in cursor.fetchall():
    print(row)
"""

# Ask a question using OpenAI's API
user_query = "Hvor mange barnehager er det i Norge?"
chat_completion = client.chat.completions.create(model="gpt-4-turbo-preview",
                                               messages = [{"role": "user", 
                                                            "content": user_query}])


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
