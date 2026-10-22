from src.NcrtPhysicsQwen3.logger import logger
# from src.NcrtPhysicsQwen3.pipeline.data_ingestion_pipeline import DataIngestionPipeline
# from src.NcrtPhysicsQwen3.pipeline.data_transformation_pipeline import DataTransformationPipeline
from src.NcrtPhysicsQwen3.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline


# STAGE_NAME = "Data Ingestion stage"
# try:
#    logger.info(f"------------------------------------  {STAGE_NAME} started --------------------------------- ") 
#    data_ingestion = DataIngestionPipeline()
#    data_ingestion.initialize()
#    logger.info(f"------------------------------------- {STAGE_NAME} completed -------------------------------n\n")
# except Exception as e:
#         logger.exception(e)
#         raise e




# STAGE_NAME = "Data transformation stage"
# try:
#    logger.info(f"------------------------------------  {STAGE_NAME} started --------------------------------- ") 
#    data_transformation = DataTransformationPipeline()
#    data_transformation.initialize()
#    logger.info(f"------------------------------------- {STAGE_NAME} completed -------------------------------n\n")
# except Exception as e:
#         logger.exception(e)
#         raise e



STAGE_NAME = "Model eval stage"

try:
   logger.info(f"------------------------------------  {STAGE_NAME} started --------------------------------- ") 
   eval_config =ModelEvaluationPipeline()
   eval_config.initialize()
   logger.info(f"------------------------------------- {STAGE_NAME} completed -------------------------------n\n")

except Exception as e:
        logger.exception(e)
        raise e
