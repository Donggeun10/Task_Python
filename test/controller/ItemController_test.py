import base64

from fastapi.testclient import TestClient

from train.app.application import app

client = TestClient(app)

def test_get_hello():
    with TestClient(app) as client:
        # basic authentication is required
        token = make_basic_auth_token("robot", "play")
        response = client.get("/hello", headers={"Authorization": f"Basic {token}"})
        assert response.status_code == 200


def test_get_app_tracking_members():
    with TestClient(app) as client:
        response = client.get("/app-tracking-members")
        assert response.status_code == 200


# generate a basic authentication token
def make_basic_auth_token(username: str, password: str) -> str:
    credentials = f"{username}:{password}"
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    return encoded_credentials