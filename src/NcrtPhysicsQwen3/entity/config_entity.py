from pathlib import Path
from pydantic import BaseModel

class DataIngestionConfig(BaseModel):
    root_dir: Path
    source_URL: str
    bucket_path: str
    data_path: str
    data_dir: Path
    
class DataTransformationConfig(BaseModel):
    root_dir: Path
    data_path: Path
    tokenizer_id: str


class ModelEvaluationConfig(BaseModel):
    root_dir: Path
    base_url: str
    llm_path: str
    dataset_path: Path





