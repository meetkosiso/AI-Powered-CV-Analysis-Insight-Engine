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
cd advance-cv-insight

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt



```markdown
### Configuration

Create a `.env` file in the root directory:

```env
# Paths
DOCS_PATH=./docs
CHROMA_PATH=./chroma_db

# LLM & Embeddings
OLLAMA_BASE_URL=http://localhost:11434
LLM_MODEL=llama3.1:8b
EMBEDDING_MODEL=BAAI/bge-small-en-v1.5



```markdown
### Run the Application

```bash
# (Optional) Manually trigger indexing when documents change
python -m app.rag.indexer

# Start the FastAPI server
uvicorn app.main:app --reload --port 8000
````

`````markdown
### Run the Application

````bash
# (Optional) Manually trigger indexing when documents change
python -m app.rag.indexer

# Start the FastAPI server
uvicorn app.main:app --reload --port 8000



```markdown
## Example API Request

```bash
curl -X POST http://localhost:8000/api/v1/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is the candidate'\''s total years of Python experience?"}'



```markdown
## 🧪 Testing

Comprehensive test suite written with **pytest**

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=app --cov-report=term-missing

# Run specific tests
pytest tests/test_indexer.py
pytest tests/api/



```markdown
## 📂 Project Structure

advance-cv-insight/
├── app/
│   ├── api/                # API routes & dependencies
│   ├── core/               # Settings & configuration
│   ├── models/             # Pydantic schemas
│   ├── prompts/            # LLM prompt templates
│   ├── rag/                # Indexing, retrieval & chain logic
│   └── main.py
├── tests/                  # pytest suite
├── docs/                   # Place your CV PDFs here
├── chroma_db/              # Chroma persistent storage (gitignored)
├── requirements.txt
````
`````

```

## 🔧 Development Tips

- Re-index documents after adding or modifying PDFs
- Delete `chroma_db/` folder when changing the embedding model
- Try stronger local models (Qwen2.5 14B, Llama 3.1 70B, etc.) for better results
- Tune retrieval parameters (`k`, ensemble weights, reranker `top_n`) for your use case


## 📈 Roadmap Ideas

- Document upload endpoint
- Multi-turn conversation support
- Support for .docx, web pages, and other formats
- Automated retrieval evaluation & A/B testing
- Docker + docker-compose deployment
```
