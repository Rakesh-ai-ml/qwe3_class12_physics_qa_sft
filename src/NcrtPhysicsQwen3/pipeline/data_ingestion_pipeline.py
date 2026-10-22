from src.NcrtPhysicsQwen3.config.configuration import ConfigurationManager
from src.NcrtPhysicsQwen3.components.data_ingestion import DataIngestion
from src.NcrtPhysicsQwen3.logger import logger

class DataIngestionPipeline:
    def __init__(self):
        pass

    def initialize(self):
        config= ConfigurationManager()
        data_ingestion_config=config.get_data_ingestion_config()
        data_ingestion=DataIngestion(config=data_ingestion_config)
        data_ingestion.download_dataset()