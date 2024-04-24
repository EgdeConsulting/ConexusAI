import os
from dotenv import load_dotenv
import urllib.parse
class Config:
    """ Klassen håndterer innlasting av konfigurasjonsdata fra miljøvariabler. """

    def __init__(self):
        print("Config init")
        load_dotenv()
        self.load_configuration()

    def load_configuration(self):
        """ Laster inn nødvendige konfigurasjonsvariabler. """
        print(" CONFIG load_configuration method called")
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.server_db = os.getenv("SERVER_DB")
        self.database_db = os.getenv("DATABASE_DB")
        self.username_db = os.getenv("USERNAME_DB")
        self.password_db = os.getenv("PASSWORD_DB")
        self.driver_db = os.getenv("DRIVER_DB")

        # Pass på at driver-navnet er korrekt URL-enkodet; for eksempel, mellomrom erstattes med '+'.
        # Eksempel for SQL Server, driveren kan være 'ODBC+Driver+17+for+SQL+Server'
        encoded_driver = urllib.parse.quote_plus(self.driver_db)

        # SQLAlchemy tilkoblingsstreng for SQL Server med dynamisk driver
        self.database_url = (
            f"mssql+pyodbc://{self.username_db}:{self.password_db}"
            f"@{self.server_db}/{self.database_db}?driver={encoded_driver}"
        )
