import os
from datasets import load_dataset
from src.NcrtPhysicsQwen3.config.configuration import DataTransformationConfig
from src.NcrtPhysicsQwen3.logger import logger
from transformers import AutoTokenizer
import boto3
from botocore.config import Config

class DataTransformation:

    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_id)

    def generate_conversation(self, examples):
        questions = examples["Question"]
        
        if isinstance(questions, str):
            questions = [questions]

        system_instruction = (
            "Follow these steps to answer the user's question:\n"
            "1. First, reason step-by-step inside <think> tags. This is your internal monologue.\n"
            "2. After the </think> tag, provide a complete, helpful, and polished answer "
            "for the user that includes both a direct answer and an explanation."
        )
        
        formatted_prompts = []

        for q in questions:
            messages = [
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": q}
            ]
                        
            prompt_str = self.tokenizer.apply_chat_template(
                messages,
                tokenize=False,
                add_generation_prompt=True
            )
            formatted_prompts.append(prompt_str)

        return {"formatted_query": formatted_prompts}
    
    def load_data(self):
        
        ds = load_dataset("csv", data_files=str(self.config.data_path))
        cols_to_remove = [
            'Topic', 'Difficulty', 'StudentLevel', 'QuestionType', 
            'QuestionComplexity', 'Prerequisites', 'EstimatedTime', 
            'subject', 'grade'
        ]
        existing_cols = ds["train"].column_names
        cols_to_drop = [c for c in cols_to_remove if c in existing_cols]
        ds = ds["train"].remove_columns(cols_to_drop)
        ds = ds.train_test_split(test_size=0.1, seed=42)
        ds = ds.map(self.generate_conversation, batched=True)
        logger.info(f"Dataset columns: {ds.column_names}")
        logger.info(f"Sample test prompt:\n{ds['test'][0]['formatted_prompt']}")
        ds["test"].save_to_disk(self.config.root_dir)
        logger.info(f"Dataset successfully transformed and saved to {self.config.root_dir}")
        ds["test"].to_csv("transformed_dataset.csv", index=False)   # or to_json / to_parquet
    
    def upload_to_bucket(self):
        self.load_data()
        s3 = boto3.client(
            "s3",
            endpoint_url="https://s3.hf.co",
            config=Config(
                region_name="us-east-1",
                s3={"addressing_style": "path"},
            ),
        )

        s3.upload_file(
            Filename="transformed_dataset.csv",   
            Bucket="Rakesh7n",              
            Key="ncrt/transformed_dataset"  
        )

    


        