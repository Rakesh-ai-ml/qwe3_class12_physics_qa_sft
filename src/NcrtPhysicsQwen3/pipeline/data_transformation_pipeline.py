from src.NcrtPhysicsQwen3.config.configuration import ConfigurationManager
from src.NcrtPhysicsQwen3.components.data_transformation import DataTransformation
# from src.NcrtPhysicsQwen3.logger import logger

class DataTransformationPipeline:
    def __init__(self):
        pass

    def initialize(self):
        config= ConfigurationManager()
        transformation_config=config.get_data_transformation_config()
        transformation=DataTransformation(config=transformation_config)
        transformation.upload_to_bucket()