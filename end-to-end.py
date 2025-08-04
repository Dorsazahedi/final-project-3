import sys
import os
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), 'order-service'))
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_order_e2e(client):
    create_response = client.post("/orders", json={"user": "e2e_user", "product": "e2e_item"})
    assert create_response.status_code == 201
    data = create_response.get_json()
    assert "order" in data
    assert data["order"]["user"] == "e2e_user"
    assert data["order"]["product"] == "e2e_item"

    get_response = client.get("/orders")
    assert get_response.status_code == 200
    orders = get_response.get_json()
    assert any(o["user"] == "e2e_user" and o["product"] == "e2e_item" for o in orders)
