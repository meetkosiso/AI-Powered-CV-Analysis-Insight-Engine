from pydantic import BaseModel
from typing import List, Optional


class QueryRequest(BaseModel):
    question: str


class Source(BaseModel):
    content: str
    source: str
    page: Optional[int] = None


class QueryResponse(BaseModel):
    answer: str
    sources: List[Source]
