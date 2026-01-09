# Advance CV Insight – AI-Powered CV Analysis & Insight Engine

Intelligent semantic search, question-answering, and insight generation over resumes and CV documents using modern Retrieval-Augmented Generation (RAG).

Built with **FastAPI** + **LangChain** + **Ollama** + **Chroma** + Hybrid Search & Reranking

## ✨ Features

- Semantic + Keyword Hybrid Search (0.7 vector / 0.3 BM25)
- FlashRank Reranking for improved relevance
- Stable, content-aware chunk IDs that survive re-indexing
- Incremental indexing with upsert (no full rebuilds)
- Fully local & offline-first (Ollama + HuggingFace embeddings)
- FastAPI REST API with clean dependency injection
- Production-oriented patterns (process-level singletons, proper error handling)

## 🛠️ Tech Stack

# Clone the repository

git clone github.com
cd advance-cv-insight

# Create and activate virtual environment

python -m venv .venv
source .venv/bin/activate # Windows: .venv\Scripts\activate

# Install dependencies

pip install -r requirements.txt

# Paths

DOCS_PATH=./docs
CHROMA_PATH=./chroma_db

# LLM & Embeddings

OLLAMA_BASE_URL=http://localhost:11434
LLM_MODEL=llama3.1:8b
EMBEDDING_MODEL=BAAI/bge-small-en-v1.5

# (Optional) Manually trigger indexing when documents change

python -m app.rag.indexer

# Start the FastAPI server

uvicorn app.main:app --reload --port 8000

# Run all tests

pytest

# Run with coverage report

pytest --cov=app --cov-report=term-missing

advance-cv-insight/
├── app/ # Main application code
│ ├── api/ # API routes & dependencies
│ ├── core/ # Settings, configuration & dependencies
│ ├── models/ # Pydantic schemas & data models
│ ├── prompts/ # LLM prompt templates
│ ├── rag/ # Indexing, retrieval, chains & RAG logic
│ └── main.py # FastAPI application entry point
├── tests/ # Test suite (pytest)
├── docs/ # Place your CV/resume PDF files here
├── chroma_db/ # Chroma vector database storage
├── requirements.txt # Python dependencies
├── .env.example # Example environment variables
└── README.md # This file
