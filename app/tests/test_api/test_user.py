from typing import Any, Dict

from fastapi.testclient import TestClient
from requests.models import Response
from sqlalchemy.orm.scoping import scoped_session
from app.tests.utils import StatusCode


def post_user(
    client: TestClient,
    db: scoped_session,
    email: str,
    password: str = "test",
    user_name: str = "田中",
) -> Response:
    data: Dict[str, Any] = {
        "user_name": user_name,
        "email": email,
        "password": password,
    }
    return client.post("/api/users/", json=data)


def test_create_user(client: TestClient, db: scoped_session) -> None:
    data: Dict[str, Any] = {
        "user_name": "山田",
        "email": "test11@example.com",
        "password": "test",
    }
    r = client.post("/api/users/", json=data)
    assert r.status_code == StatusCode.OK

    resp: Dict[str, Any] = r.json()
    assert resp["email"] == data["email"]


def test_read_user(client: TestClient, db: scoped_session) -> None:
    id: int = 1
    r = client.get(f"/api/users/{id}")
    assert r.status_code == StatusCode.OK


# 登録済みのemailでの登録をはじく
def test_create_user_error(client: TestClient, db: scoped_session) -> None:
    r = post_user(client=client, db=db, email="test11@example.com")
    r.status_code == StatusCode.BadRequest


def test_delete_user_error(client: TestClient, db: scoped_session) -> None:
    id: int = 100
    r = client.delete(f"/api/users/{id}")
    assert r.status_code == StatusCode.NotFound


def test_delete_user(client: TestClient, db: scoped_session) -> None:
    r = client.delete("/api/users/2")
    assert r.status_code == StatusCode.OK
