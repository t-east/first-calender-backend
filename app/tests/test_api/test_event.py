from typing import Any, Dict

import requests
from fastapi.testclient import TestClient
from sqlalchemy.orm.scoping import scoped_session
from app.tests.utils import StatusCode


def post_event(
    client: TestClient,
    db: scoped_session,
    from_date: str,
    to_date: str,
    user_id: int,
    title: str = "タイトル",
    description_text: str = "内容",
    is_all_day: bool = False,
) -> requests.Response:
    data: Dict[str, Any] = {
        "from_date": from_date,
        "to_date": to_date,
        "user_id": user_id,
        "title": title,
        "description_text": description_text,
        "is_all_day": is_all_day,
    }
    return client.post("/api/events/", data=data)


def test_post_event(client: TestClient, db: scoped_session) -> None:
    data: Dict[str, Any] = {
        "user_id": 1,
        "title": "タイトル",
        "description_text": "内容",
        "from_date": "2022-03-20T15:47:04.097Z",
        "is_all_day": False,
        "to_date": "2022-03-20T15:47:04.097Z",
    }
    r = client.post("/api/events/", json=data)
    assert r.status_code == StatusCode.OK


# def test_post_event_error_not_exist(client: TestClient) -> None:
#     data: Dict[str, Any] = {
#         "title": "タイトル",
#         "description_text": "内容",
#         "from_date": "2021-10-20T13:00:00",
#         "is_all_day": True,
#         "to_date": "2021-10-10T13:00:00",
#     }
#     r: requests.Response = client.post("/api/event/", data=data)
#     assert r.status_code == StatusCode.Unauthorized


def test_post_event_invalid_date(client: TestClient, db: scoped_session) -> None:
    data: Dict[str, Any] = {
        "user_id": 1,
        "title": "タイトル",
        "description_text": "内容",
        "from_date": "2022-03-23T15:47:04.097Z",
        "is_all_day": False,
        "to_date": "2022-03-20T15:47:04.097Z",
    }
    r = client.post("/api/events/", json=data)
    assert r.status_code == StatusCode.BadRequest


# def test_get_event_list_by_user_id(client: TestClient, db: scoped_session) -> None:
#     user_id = 1
#     r: requests.Response = client.get(f"/api/event/{user_id}")
#     assert r.status_code == StatusCode.OK


def test_get_event_list(client: TestClient, db: scoped_session) -> None:
    r: requests.Response = client.get("/api/events/")
    assert r.status_code == StatusCode.OK


def test_get_event_list_by_user_id(client: TestClient, db: scoped_session) -> None:
    user_id = 1
    r: requests.Response = client.get(f"/api/events/{user_id}")
    assert r.status_code == StatusCode.OK


def test_get_event_list_by_user_id_error(
    client: TestClient, db: scoped_session
) -> None:
    user_id = 100
    r: requests.Response = client.get(f"/api/events/{user_id}")
    assert r.status_code == StatusCode.BadRequest


def test_get_event(client: TestClient, db: scoped_session) -> None:
    event_id = 1
    # user_id = 1
    r: requests.Response = client.get(f"/api/events/{event_id}")
    assert r.status_code == StatusCode.OK


def test_get_event_error(client: TestClient, db: scoped_session) -> None:
    event_id = 100
    # user_id = 1
    r: requests.Response = client.get(f"/api/events/{event_id}")
    assert r.status_code == StatusCode.BadRequest


def test_delete_event(client: TestClient, db: scoped_session) -> None:
    event_id: int = 1
    user_id: int = 1
    r: requests.Response = client.delete(f"/api/events/{user_id}/{event_id}")
    assert r.status_code == StatusCode.OK


def test_delete_event_error_invalid_user(
    client: TestClient, db: scoped_session
) -> None:
    event_id = 1
    user_id = 100
    r: requests.Response = client.delete(f"/api/events/{user_id}/{event_id}")
    assert r.status_code == StatusCode.Unauthorized


def test_delete_event_error(client: TestClient, db: scoped_session) -> None:
    event_id = 100
    user_id = 1
    r: requests.Response = client.delete(f"/api/events/{user_id}/{event_id}")
    assert r.status_code == StatusCode.BadRequest
