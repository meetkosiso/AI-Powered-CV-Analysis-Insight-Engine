from langchain_community.document_loaders import DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from app.core.config import settings
import hashlib
import os


class DocumentIndexer:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL)
        self.db_path = settings.CHROMA_PATH

    def _chunk_id(self, source: str, page: int, chunk_index: int) -> str:
        """Generate a stable, content-aware ID for a chunk."""
        content_hash = hashlib.sha256(
            f"{source}:{page}:{chunk_index}".encode("utf-8")
        ).hexdigest()[:16]
        safe_source = os.path.basename(source).replace(".", "_")
        return f"{safe_source}_p{page}_c{chunk_index}_{content_hash}"

    def build_or_load_index(self) -> Chroma:
        loader = DirectoryLoader(
            settings.DOCS_PATH, glob="**/*.pdf", show_progress=True)
        docs = loader.load()

        if not docs:
            raise ValueError(
                "No PDF documents found in the specified directory.")

        splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(docs)

        # Generate IDs
        for i, chunk in enumerate(chunks):
            source = chunk.metadata.get("source", "unknown")
            page = chunk.metadata.get("page", 0)
            chunk.metadata["id"] = self._chunk_id(source, page, i)

        db = Chroma(
            persist_directory=self.db_path,
            embedding_function=self.embeddings,
        )

        # Incremental upsert based on IDs
        db.add_documents(
            chunks,
            ids=[chunk.metadata["id"] for chunk in chunks],
        )

        print(
            f"Index updated: {len(chunks)} chunks processed → total {db._collection.count()} in DB")

        return db
