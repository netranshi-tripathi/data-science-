import sys
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project.components.data_ingestion import DataIngestionConfig

if __name__ == "__main__":
    logging.info("Starting the application...")
    try:
       # data_ingestion_config = DataIngestionConfig()
        data_ingestion= DataIngestion()
        data_ingestion.initiate_data_ingestion()
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e, sys) 

       
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e, sys) 
