import requests

def test_notification_service():
    response = requests.post("http://localhost:5002/notify/email", json={
        "user": "integration@example.com",
        "message": "This is an integration test message"
    })
    assert response.status_code == 200
    assert "email sent" in response.text.lower()
