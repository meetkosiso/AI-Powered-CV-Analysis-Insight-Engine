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

| Component           | Technology                             | Purpose                                |
| ------------------- | -------------------------------------- | -------------------------------------- |
| Backend             | FastAPI                                | High-performance API                   |
| LLM                 | Ollama (local)                         | Answer generation                      |
| Embeddings          | HuggingFace sentence-transformers      | Dense vector generation                |
| Vector Store        | Chroma                                 | Persistent local vector database       |
| Retrieval           | LangChain (Ensemble + Compression)     | Hybrid search + reranking              |
| Reranker            | FlashRank                              | Fast & lightweight relevance reranking |
| Document Processing | PyPDF + RecursiveCharacterTextSplitter | PDF loading & intelligent chunking     |

## 🚀 Quick Start

### Prerequisites

- Python 3.9–3.12
- Ollama installed and running locally with a model pulled  
  (example: `ollama pull llama3.1:8b` or `qwen2.5:7b`)
- Some PDF resumes/CVs placed in the `docs/` folder

### Installation

````bash
# Clone the repository
git clone https://github.com/YOUR-USERNAME/advance-cv-insight.git
cd advance-cv-insight

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt



```markdown
### Configuration

Create a `.env` file in the root directory with the following content:

```env
# Paths
DOCS_PATH=./docs
CHROMA_PATH=./chroma_db

# LLM & Embeddings
OLLAMA_BASE_URL=http://localhost:11434
LLM_MODEL=llama3.1:8b
EMBEDDING_MODEL=BAAI/bge-small-en-v1.5


### Run the Application

```bash
# (Optional) Manually trigger indexing when documents change
python -m app.rag.indexer

# Start the FastAPI server
uvicorn app.main:app --reload --port 8000



### Full context example (how it fits in the Quick Start section):

```markdown
## 🚀 Quick Start

### Prerequisites

- Python 3.9–3.12
- Ollama installed and running locally with a model pulled
  (example: `ollama pull llama3.1:8b` or `qwen2.5:7b`)
- Some PDF resumes/CVs placed in the `docs/` folder

### Installation

```bash
# Clone the repository
cd advance-cv-insight

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt


## Example API Request

```bash
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the candidate'\''s total years of Python experience?"}'



## 🧪 Testing

Comprehensive test suite written with **pytest**

```bash
# Run all tests
pytest

# Run with coverage report (shows which lines are not tested)
pytest --cov=app --cov-report=term-missing

# Run tests from a specific file
pytest tests/test_indexer.py

# Run tests from a specific directory
pytest tests/api/


## 📂 Project Structure

```text
advance-cv-insight/
├── app/                    # Main application code
│   ├── api/                # API routes & dependencies
│   ├── core/               # Settings, configuration & dependencies
│   ├── models/             # Pydantic schemas & data models
│   ├── prompts/            # LLM prompt templates
│   ├── rag/                # Indexing, retrieval, chains & RAG logic
│   └── main.py             # FastAPI application entry point
├── tests/                  # Test suite (pytest)
│   ├── api/                # API endpoint tests
│   └── test_indexer.py     # Document indexing tests
├── docs/                   # Place your CV/resume PDF files here
├── chroma_db/              # Chroma vector database storage (gitignored)
├── requirements.txt        # Python dependencies
├── .env.example            # Example environment variables (recommended)
└── README.md               # This file
````
