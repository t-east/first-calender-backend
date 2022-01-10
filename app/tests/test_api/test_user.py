import random
import string
from typing import Any, Dict, List, Tuple

import requests
from fastapi.testclient import TestClient
from requests.models import Response

from app.tests.utils import StatusCode


def post_user(
    client: TestClient, email: str, password: str = "test", user_name: str = "田中"
) -> Response:
    data: Dict[str, Any] = {
        "user_name": user_name,
        "email": email,
        "password": password,
    }
    return client.post("/api/user/", json=data)


def test_create_user(client: TestClient) -> None:
    data: Dict[str, Any] = {
        "user_name": "山田",
        "email": "test@example.com",
        "password": "test",
    }
    r = client.post("/api/user/", json=data)
    assert r.status_code == StatusCode.OK

    resp: Dict[str, Any] = r.json()
    for key in ("email", "birthday"):
        assert resp[key] == data[key]


# 登録済みのemailでの登録をはじく
def test_create_user_error(client: TestClient) -> None:
    r = post_user(client=client, email="test@example.com")
    r.status_code == StatusCode.BadRequest


def test_delete_user_error(client: TestClient) -> None:
    r = client.delete("/api/user/100")
    assert r.status_code == StatusCode.Unauthorized


def test_delete_user(client: TestClient) -> None:
    r = client.delete("/api/user/2")
    assert r.status_code == StatusCode.Unauthorized
