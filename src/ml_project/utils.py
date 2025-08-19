import os
import sys
from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
import pandas as pd
from dotenv import load_dotenv
import pymysql

# Load environment variables from .env file
load_dotenv()  
host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")


def read_sql_data():
    logging.info("Reading data from MySQL database")
    try: 
        mydb = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db
        )
        logging.info(f"Connected to the database successfully: {db} at {host}")

        df = pd.read_sql_query("SELECT * FROM student", mydb)
        print(df.head())

        mydb.close()   # Always close the connection
        return df
    
    except Exception as ex:
        raise CustomException(ex, sys)
