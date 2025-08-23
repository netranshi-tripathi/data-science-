import os
import sys
from src.ml_project.exception import CustomException
from src.ml_project.logger import logging
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score
import pandas as pd
from dotenv import load_dotenv
import pymysql
import pickle
import numpy as np

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
    
def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, "wb") as f:
            pickle.dump(obj, f)
    except Exception as e:
        raise CustomException(e, sys) from e
    
def evaluate_models(X_train, y_train, X_test, y_test, models, params):
    try:
        report = {}
        for i in range(len(list(models))):
            model = list(models.values())[i]
            param = params[list(models.keys())[i]]
            # Here we can add hyperparameter tuning if needed
            gs= GridSearchCV(model,param,cv=3)
            gs.fit(X_train,y_train)
           
            model.set_params(**gs.best_params_)
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)
            y_test_pred = model.predict(X_test)
            train_model_score = r2_score(y_train, y_train_pred)
            test_model_score = r2_score(y_test, y_test_pred)
            report[list(models.keys())[i]] = test_model_score
        return report
    except Exception as e:
        raise CustomException(e, sys)