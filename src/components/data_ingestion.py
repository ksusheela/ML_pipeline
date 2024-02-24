import os,sys
from src.logger import logging
from src.exception import CustomException
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig
from src.utils import read_yaml_file, get_collection_as_dataframe
import pandas as pd
import numpy as np
import shutil
from sklearn.model_selection import train_test_split
from src.constant import *



class DataIngestion:
    def __init__(self, data_ingestion_config: DataIngestionConfig):
        try:
            logging("***************Data Ingestion Stsrted *************************")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)
        

# get the data from the databases / fetch the data from the databases [MongoDB]
# split the data into Train and test
#intiate data ingestion steps
        
    def get_data_from_mongo(self):
        df:pd.DataFrame = get_collection_as_dataframe(
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingetion_config.collection_name

        )
        
            
            
        raw_data_dir =self.data_ingestion_config.raw_data_dir

        os.makedirs(raw_data_dir, exist_ok=True)

        csv_file_name = "train.csv"
        csv_file_new = "tests.csv"

        raw_file_path = os.path.join(raw_data_dir, csv_file_name)

        df.to_csv(raw_file_path)

        ingested_directory = os.path.join(self.data_ingestion_config.ingested_data_dir)
        os.makedir(ingested_directory, exist_ok = True)

        ingested_file_path = os.path.join(self.data_ingestion_config.ingested_data_dir,csv_file_name)

        shutil.copy(raw_file_path, ingested_file_path)

        return ingested_file_path
    
    def split_csv_to_train_test(self, csv_file_name):


        train_file_path = self.data_ingestion_config.trin_file_path
        test_file_path = self.data_ingestion_config.test_file_path
        
        os.makedirs(train_file_path)
        os.makedirs(test_file_path)

        data =pd.read_csv(csv_file_name, index_col=0)

        size =self.data_ingestion_config.test_size

        train_data, test_data = train_test_split(data, test_size=size, random_state=42)

        #saving data
        train_file_path = os.path.join(train_file_path, FILE_NAME)
        test_file_path = os.path.join(test_file_path, FILE_NAME)

        train_data.to_csv(train_file_path)
        test_data.to.csv(test_file_path)

        data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path, test_file_path=test_file_path)
        return data_ingestion_artifact
    
    def initiate_data_ingestion(self):
        try:
            ingested_file_path = self.get_data_from_mongo()
            return self.split_csv_to_train_test(csv_file_name=ingested_file_path)
        except Exception as e:
            raise CustomException(e,sys) from e

