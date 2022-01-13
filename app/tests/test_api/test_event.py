from typing import Any, Dict

import requests
from fastapi.testclient import TestClient

from app.tests.utils import StatusCode


def post_event(
    client: TestClient,
    begin_date_: str,
    end_date_: str,
    user_id: int,
    title: str = "タイトル",
    description: str = "内容",
    is_all_day: bool = False,
) -> requests.Response:
    data: Dict[str, Any] = {
        "begin_date_": begin_date_,
        "end_date_": end_date_,
        "user_id": user_id,
        "title": title,
        "description": description,
        "is_all_day": is_all_day,
    }
    return client.post("/api/event/", data=data)


def test_post_event(client: TestClient) -> None:
    data: Dict[str, Any] = {
        "title": "タイトル",
        "description": "内容",
        "begin_date_": "2021-10-20T13:00:00",
        "is_all_day": True,
        "end_date_": "2021-10-10T13:00:00",
        "user_id": 1,
    }
    r: requests.Response = client.post("/api/event/", data=data)
    assert r.status_code == StatusCode.OK


def test_post_event_error_not_exist(client: TestClient) -> None:
    data: Dict[str, Any] = {
        "title": "タイトル",
        "description": "内容",
        "begin_date_": "2021-10-20T13:00:00",
        "is_all_day": True,
        "end_date_": "2021-10-10T13:00:00",
        "user_id": 3,
    }
    r: requests.Response = client.post("/api/event/", data=data)
    assert r.status_code == StatusCode.Unauthorized


def test_post_event_invalid_date(client: TestClient) -> None:
    data: Dict[str, Any] = {
        "title": "タイトル",
        "description": "内容",
        "begin_date_": "2021-10-20T13:00:00",
        "is_all_day": True,
        "end_date_": "2021-10-10T13:00:00",
        "user_id": 3,
    }
    r: requests.Response = client.post("/api/event/", data=data)
    assert r.status_code == StatusCode.BadRequest


def test_get_event_list__by_user_id(client: TestClient) -> None:
    # user_id = 1
    r: requests.Response = client.get("/api/event/")
    assert r.status_code == StatusCode.OK


def test_get_event_list__by_user_id_error(client: TestClient) -> None:
    # user_id = 100
    r: requests.Response = client.get("/api/event/")
    assert r.status_code == StatusCode.OK


def test_get_event(client: TestClient) -> None:
    event_id = 1
    # user_id = 1
    r: requests.Response = client.get(f"/api/event/{event_id}")
    assert r.status_code == StatusCode.OK


def test_get_event_error_invalid_user(client: TestClient) -> None:
    event_id = 1
    # user_id = 2
    r: requests.Response = client.get(f"/api/event/{event_id}")
    assert r.status_code == StatusCode.BadRequest


def test_get_event_error(client: TestClient) -> None:
    event_id = 100
    # user_id = 1
    r: requests.Response = client.get(f"/api/event/{event_id}")
    assert r.status_code == StatusCode.BadRequest


def test_delete_event_error_invalid_user(client: TestClient) -> None:
    event_id = 1
    # user_id = 2
    r: requests.Response = client.delete(f"/api/event/{event_id}")
    assert r.status_code == StatusCode.BadRequest


def test_delete_event_error(client: TestClient) -> None:
    event_id = 100
    # user_id = 1
    r: requests.Response = client.delete(f"/api/event/{event_id}")
    assert r.status_code == StatusCode.BadRequest


def test_delete_event(client: TestClient) -> None:
    event_id = 1
    # user_id = 1
    r: requests.Response = client.delete(f"/api/event/{event_id}")
    assert r.status_code == StatusCode.OK
