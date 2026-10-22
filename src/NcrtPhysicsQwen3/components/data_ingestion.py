import os
import boto3
from botocore.config import Config
from src.NcrtPhysicsQwen3.config.configuration import DataIngestionConfig
from src.NcrtPhysicsQwen3.logger import logger
from dotenv import load_dotenv
load_dotenv()

class DataIngestion:
    
    def __init__(self,config : DataIngestionConfig):
        self.config=config

    def download_dataset(self):          
        s3 = boto3.client(
            "s3",
            endpoint_url= self.config.source_URL,
            config=Config(
                region_name="us-east-1",
                s3={"addressing_style": "path"},
                request_checksum_calculation="when_required",
                response_checksum_validation="when_required",
            ),
        )

        local_file = os.path.join(
                    self.config.data_dir,
                    os.path.basename(self.config.data_path)
        )

        s3.download_file(self.config.bucket_path, self.config.data_path, local_file)
        logger.info("Dataset downloaded successfully from Huggingface bucket")
