from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    LLM_MODEL: str = "llama3.1:8b"
    EMBEDDING_MODEL: str = "BAAI/bge-small-en-v1.5"
    CHROMA_PATH: str = "data/chroma_db"
    DOCS_PATH: str = "docs/"
    OLLAMA_BASE_URL: str = "http://localhost:11434"


settings = Settings()
