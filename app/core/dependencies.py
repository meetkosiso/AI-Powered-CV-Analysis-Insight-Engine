from typing import Optional
from fastapi import Depends
from langchain_community.llms import Ollama
from langchain_chroma import Chroma
from app.rag.chain import build_rag_chain
from app.rag.ingestion import DocumentIndexer
from app.core.config import settings


# Module-level singletons, created once per process
_llm: Optional[Ollama] = None
_db: Optional[Chroma] = None
_rag_chain: Optional[object] = None


def get_llm() -> Ollama:
    """Return a shared Ollama LLM instance."""
    global _llm
    if _llm is None:
        _llm = Ollama(
            model=settings.LLM_MODEL,
            temperature=0.2,
            base_url=settings.OLLAMA_BASE_URL,
        )
    return _llm


def get_indexer() -> DocumentIndexer:
    """Lightweight factory, creates new instance each time it's needed."""
    return DocumentIndexer()


def get_db(indexer: DocumentIndexer = Depends(get_indexer)) -> Chroma:
    """Return a shared Chroma instance (indexed once per process)."""
    global _db
    if _db is None:
        _db = indexer.build_or_load_index()
    return _db


def get_rag_chain(
    db: Chroma = Depends(get_db),
    llm: Ollama = Depends(get_llm),
) -> object:
    """Return a shared RAG chain, built once per process."""
    global _rag_chain
    if _rag_chain is None:
        _rag_chain = build_rag_chain(db=db, llm=llm)
    return _rag_chain
