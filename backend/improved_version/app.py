# Define the connection string
server = 'tcp:datavarehusetdb.database.windows.net,1433'
database = 'asql-processed-prod-dw-2024-2-13-17-9'
username = 'egdeadmin'
password = 'ConexusAIDB2024'
driver = '{ODBC Driver 18 for SQL Server}'
connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'
