import mysql.connector
from dotenv import load_dotenv
import os

def game_monitoring_connector():
    # Load the variables from .env file
    load_dotenv()

    # Access environment variables
    db_host = os.getenv('DB_HOST')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_name = os.getenv('DB_NAME')

    db_connection = mysql.connector.connect(
        host = db_host,
        user = db_user,
        password = db_password,
        database = db_name
    )
    
    print(f"Connected to database {db_name} at {db_host} with user {db_user}")
    return db_connection
