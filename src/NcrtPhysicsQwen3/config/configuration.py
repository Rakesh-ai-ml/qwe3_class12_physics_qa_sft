import os
from src.NcrtPhysicsQwen3.utils.common import read_yaml, create_directories
from src.NcrtPhysicsQwen3.entity.config_entity import (
                                                        DataIngestionConfig,
                                                        DataTransformationConfig,
                                                        ModelEvaluationConfig
                                                    )
from src.NcrtPhysicsQwen3.constants.constants import CONFIG_FILE_PATH
                                                


class ConfigurationManager:

    def __init__(
                self,
                config_filepath=CONFIG_FILE_PATH,
                ):
        
        self.config=read_yaml(config_filepath)
        create_directories([self.config.artifacts_root])

                
    def get_data_ingestion_config(self)-> DataIngestionConfig:
        config=self.config
        create_directories([config.data_ingestion.root_dir])
        return DataIngestionConfig(**self.config.data_ingestion)

    
    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config
        create_directories([config.data_transformation.root_dir])
        return DataTransformationConfig(**self.config.data_transformation)


    def get_model_evaluation_config(self) ->ModelEvaluationConfig:
        config=self.config
        create_directories([config.model_evaluation.root_dir])
        return ModelEvaluationConfig(**self.config.model_evaluation)
        
        
