import sys
from src.ml_project.components import data_ingestion
from src.ml_project.logger import logging
from src.ml_project.exception import CustomException
from src.ml_project.components.data_ingestion import DataIngestion
from src.ml_project.components.data_transformation import DataTransformationConfig, DataTransformation
from src.ml_project.components.data_ingestion import DataIngestionConfig


if __name__ == "__main__":
    logging.info("Starting the application...")
    try:
       # data_ingestion_config = DataIngestionConfig()
        data_ingestion= DataIngestion()
        train_data_path, test_data_path = data_ingestion.initiate_data_ingestion()

       # data_transformation_config = DataTransfortionConfig()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(
            train_path=train_data_path,
            test_path=test_data_path
            )

    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e, sys) 

       
    except Exception as e:
        logging.info("custom exception")
        raise CustomException(e, sys) 
