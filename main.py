from networksecurity.components.data_ingestion import DataIngestion
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

if __name__=='__main__':
    try:
        training_PipelineConfig=TrainingPipelineConfig()
        data_ingestion_config = DataIngestionConfig(training_PipelineConfig)
        data_ingestion= DataIngestion(data_ingestion_config)

        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        print(dataingestionartifact)
    except Exception as e:
           raise NetworkSecurityException(e,sys)