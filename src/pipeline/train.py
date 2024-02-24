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
from src.entity.config_entity import DataIngestionConfig, TrainingPipelineConfig
from src.components.data_ingestion import DataIngestion
from src.components.data_ingestion import DataIngestion

class pipeline():
    def __init__(self, trainig_pipeline_config = TrainingPipelineConfig())->None: 

        try:
            self.trining_pipeline_config = trainig_pipeline_config
            #self.training_pipeline_config =TrainingPipelineConfig

        except Exception as e:
            raise CustomException(e,sys) from e
        
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config = DataIngestionConfig(self.trining_pipeline_config))
            
            return data_ingestion.initiate_data_ingestion()
        
        except Exception as e:
            raise CustomException(e,sys) from e
        

    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise CustomException(e,sys) from e


            




        