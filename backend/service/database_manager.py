from langchain_community.utilities import SQLDatabase
from sqlalchemy import create_engine
from .config import Config
from sqlalchemy.sql import text
class DatabaseWrapper(SQLDatabase):
    def __init__(self):
        print("DatabaseWrapper init")
        config = Config()
        self.engine = create_engine(config.database_url)
        super().__init__(engine=self.engine)

    def get_connection(self):
        """ Etablerer en forbindelse til databasen. """
        print("DAABASE get_connection method called")
        return self.engine.connect()

    def run_query(self, query):
        """ Utfører en SQL-spørring og returnerer resultatene. """
        print(" DAABASE run_query method called query: ",{query})    
        with self.get_connection() as conn:
            result = conn.execute(text(query))
            print("DAABASE run_query method called result:", {result})
            return [row for row in result]

    def get_table_info(self):
        """ Henter informasjon om databasetabeller """
        print("DAABASE get_table_info method called", )
        query = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' AND TABLE_TYPE = 'BASE TABLE'"
        print("DAABASE get_table_info method called", {query})
        return self.run_query(query)
