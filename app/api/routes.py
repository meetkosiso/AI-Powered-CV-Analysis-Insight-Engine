from fastapi import APIRouter, Depends, HTTPException
from loguru import logger

from app.models.schemas import QueryRequest, QueryResponse, Source
from app.core.dependencies import get_rag_chain


router = APIRouter(prefix="/api/v1", tags=["query"])


@router.post("/query", response_model=QueryResponse)
async def query(
    request: QueryRequest,
    rag_chain=Depends(get_rag_chain),
):
    """
    Answer a user question using the RAG pipeline.

    Returns the generated answer plus a list of source chunks (truncated)
    that contributed to the response.
    """
    if not request.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")

    try:
        logger.info("Processing query: {q}", q=request.question[:200])

        result = await rag_chain.ainvoke({"input": request.question})

        # LangChain retrieval chain returns dict with answer and context
        answer = result["answer"]
        context_docs = result.get("context", [])

        sources = [
            Source(
                content=doc.page_content[:500] +
                ("..." if len(doc.page_content) > 500 else ""),
                source=doc.metadata.get("source", "unknown").split(
                    "/")[-1],
                page=doc.metadata.get("page"),
            )
            for doc in context_docs
        ]

        logger.info(
            "Query completed | sources={n} | answer_length={l}",
            n=len(sources),
            l=len(answer),
        )

        return QueryResponse(answer=answer, sources=sources)

    except Exception as exc:
        logger.exception("RAG query failed: {exc}", exc=exc)
        raise HTTPException(
            status_code=500, detail="Failed to process query") from exc
