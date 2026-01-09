from app.rag.ingestion import DocumentIndexer
from app.core.config import settings
import os
import shutil


def test_document_indexing(tmp_path, monkeypatch):
    monkeypatch.setattr(settings, "CHROMA_PATH", str(tmp_path / "test_db"))
    monkeypatch.setattr(settings, "DOCS_PATH", "docs/")

    indexer = DocumentIndexer()
    db = indexer.build_or_load_index()

    assert db._collection.count() > 0  # At least one chunk from CV
    assert os.path.exists(tmp_path / "test_db")
