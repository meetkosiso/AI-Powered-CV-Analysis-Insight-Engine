import pytest


@pytest.mark.asyncio
async def test_query_endpoint(client):
    response = client.post("/query", json={"question": "What is my name?"})

    assert response.status_code == 200
    data = response.json()
    assert "answer" in data
    assert "sources" in data
    assert isinstance(data["sources"], list)


def test_health_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ready"
