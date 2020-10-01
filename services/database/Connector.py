import mysql.connector
from dotenv import load_dotenv
from pathlib import Path
import os

class DBConnector:
    
    def __init__(self):
        env_path = Path('.') / '.env'
        load_dotenv(dotenv_path=env_path)
        
        mydb = mysql.connector.connect(
            host = os.getenv("DB_HOST"),
            database = os.getenv("DB_DATABASE"),
            user= os.getenv("DB_USERNAME"),
            password = os.getenv("DB_PASSWORD")
        )

        self.connection = mydb.cursor()

