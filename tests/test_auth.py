from fastapi.testclient import TestClient
from app.main import app  # Asegúrate de que este import apunte a tu archivo principal

client = TestClient(app)

# Datos de prueba
user_data = {
    "name": "Ana Torres",
    "email": "anas3@example.com",
    "password": "12345678909",
    "phone": "3023550691",
    "notification_preference": "sms",
    "identification": "1234567890"
}

def test_signup():
    response = client.post("/auth/signup", json=user_data)

    print("Signup response:", response.json())

    # Puede ser 200 OK si se crea, o 409 si ya existe
    assert response.status_code in [200, 409]


def test_login():
    login_data = {
        "username": user_data["email"],
        "password": user_data["password"]
    }

    response = client.post("/auth/login", data=login_data)

    print("Login response:", response.json())

    assert response.status_code == 200
    assert "access_token" in response.json()
