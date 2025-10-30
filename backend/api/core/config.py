"""
Configuration Management
Simple settings for MVP
"""

import os
from pathlib import Path

# API Keys
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Paths
BASE_DIR = Path(__file__).resolve().parent.parent.parent
UPLOAD_DIR = BASE_DIR / "uploads"
VECTOR_STORE_DIR = BASE_DIR / "rag" / "embeddings" / "vector_store"
LOGS_DIR = BASE_DIR / "logs"

# Create directories
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
VECTOR_STORE_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# RAG Settings
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
TOP_K_RESULTS = 5

# Allowed file types
ALLOWED_EXTENSIONS = {'.py', '.js', '.java', '.txt', '.md', '.json'}

print("✓ Configuration loaded")
print(f"✓ Upload directory: {UPLOAD_DIR}")
print(f"✓ Vector store: {VECTOR_STORE_DIR}")