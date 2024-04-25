import os
from dotenv import load_dotenv
from app import connection_string
from sqlalchemy import create_engine, text
import json
import pyodbc

conn_string = 'mssql+pyodbc:///?odbc_connect=' + connection_string

engine = create_engine(conn_string)

try:
    # Function to retrieve data from the dim_indikator table
    def get_dim_indikator_data(keyword):
        query = """
            SELECT [navn], [maaleenhet], [human_readable_table_name], [eier], [eierbeskrivelse], [eierSistEndret], [fraDato], [tilDato], [fagomraade], [dim_indikator_key], [eierbeskrivelseURL], [aktiv]
            FROM [dbo].[dim_indikator]
            WHERE navn LIKE '%keyword%'
               OR eierbeskrivelse LIKE :keyword
               OR human_readable_table_name LIKE :keyword
               OR fagomraade LIKE :keyword
        """
        with engine.connect() as conn:
            result = conn.execute(text(query), keyword=f"%{keyword}%")
            #result = conn.execute(text(query), {'keyword': f"%{keyword}%"})
            return [dict(row) for row in result]

    # Example usage
    keyword = 'barnehagelærer'
    data = get_dim_indikator_data(keyword)
    print(data)

    # Write the data to a JSON file
    with open("dim_indikator_data.json", "w") as file:
        json.dump(data, file, indent=2)

except Exception as e:
    print(f"An error occurred: {str(e)}")


