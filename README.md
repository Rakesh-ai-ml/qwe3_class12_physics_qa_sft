# NCERT Physics Qwen3 SFT

A modular pipeline for supervised fine-tuning (SFT) and evaluation of **Qwen3-4B-Thinking** on Class 12 NCERT Physics Question-Answering data.

---

## Overview

- **Base Model**: `Qwen/Qwen3-4B-Thinking-2507`
- **Training Method**: Parameter-Efficient Fine-Tuning (PEFT / LoRA 4-bit) with Unsloth
- **Format**: Step-by-step reasoning within `<think>` tags followed by structured answers and explanations
- **Evaluation**: Ragas and LLM-as-a-judge for factual correctness and answer relevancy
- **Experiment Tracking**: Weights & Biases (W&B)

---

## Project Structure

```text
├── artifacts/              # Ingested datasets, transformations, and evaluation outputs
├── config/                 # YAML configuration files (config.yaml)
├── src/NcrtPhysicsQwen3/   # Core source code
│   ├── components/         # Ingestion, transformation, training, and evaluation logic
│   ├── config/             # Configuration management
│   ├── entity/             # Pydantic schemas and data classes
│   ├── pipeline/           # Stage pipelines (ingestion, transformation, evaluation)
│   └── utils/              # Helper utilities and loggers
├── main.py                 # Pipeline execution entrypoint
└── pyproject.toml          # Project dependencies and package metadata
```

---

## Pipeline Workflow

1. **Data Ingestion**: Downloads the cleaned Class 12 NCERT Physics dataset from Hugging Face S3 storage.
2. **Data Transformation**: Converts Q&A pairs into chat-templated prompts with reasoning instructions (`<think>`) and creates train/test splits.
3. **Model Training**: Runs 4-bit quantized LoRA fine-tuning using Unsloth, logging training loss and model checkpoints to W&B.
4. **Model Evaluation**: Generates predictions from base vs. fine-tuned adapter models and evaluates factual correctness using Ragas.

---
