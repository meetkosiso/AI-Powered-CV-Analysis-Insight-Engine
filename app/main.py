from fastapi import FastAPI
from app.api.routes import router
from app.core.config import settings

app = FastAPI(
    title="Advance CV Insight using RAG",
    description="AI-powered CV Q&A with hybrid retrieval, reranking, and citations",
    version="1.0"
)

app.include_router(router)


@app.get("/")
def health():
    return {"status": "ready", "model": settings.LLM_MODEL}
