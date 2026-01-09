from unittest.mock import MagicMock, patch
from app.rag.chain import build_rag_chain
from app.core.dependencies import get_llm


def test_rag_chain_returns_answer_and_sources():
    # Create mocks
    mock_db = MagicMock()
    mock_llm = MagicMock()

    # Mock the full chain invoke to return expected structure
    mock_chain = MagicMock()
    mock_context_doc = MagicMock()
    mock_context_doc.page_content = "John Doe has 10 years in software engineering."
    mock_context_doc.metadata = {"source": "your_cv.pdf", "page": 1}

    mock_chain.invoke.return_value = {
        "answer": "John Doe has 10 years in software engineering.",
        "context": [mock_context_doc]
    }

    # Patch only the chain creation functions at module level
    with patch("app.rag.chain.create_retrieval_chain", return_value=mock_chain), \
            patch("app.rag.chain.create_stuff_documents_chain", return_value=MagicMock()):

        chain = build_rag_chain(mock_db, mock_llm)
        response = chain.invoke({"input": "How many years of experience?"})

        assert "answer" in response
        assert "context" in response
        assert len(response["context"]) > 0
        assert isinstance(response["answer"], str)
