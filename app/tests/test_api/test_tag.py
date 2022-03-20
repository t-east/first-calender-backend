from typing import Any, Dict

import requests
from fastapi.testclient import TestClient
from sqlalchemy.orm.scoping import scoped_session
from app.tests.utils import StatusCode


def post_tag(
    client: TestClient,
    db: scoped_session,
    label: str,
    color: str,
    event_id: int,
) -> requests.Response:
    data: Dict[str, Any] = {
        "label": label,
        "color": color,
        "event_id": event_id,
    }
    return client.post("/api/tags/", data=data)


def test_post_tag(client: TestClient, db: scoped_session) -> None:
    data: Dict[str, Any] = {
        "event_id": 1,
        "label": "タイトル",
        "color": "ffffff",
    }
    r = client.post("/api/tags/", json=data)
    assert r.status_code == StatusCode.OK


# def test_post_event_error_not_exist(client: TestClient) -> None:
#     data: Dict[str, Any] = {
#         "label": "タイトル",
#         "description_text": "内容",
#         "from_date": "2021-10-20T13:00:00",
#         "is_all_day": True,
#         "to_date": "2021-10-10T13:00:00",
#     }
#     r: requests.Response = client.post("/api/event/", data=data)
#     assert r.status_code == StatusCode.Unauthorized


# def test_post_tag_invalid_date(client: TestClient, db: scoped_session) -> None:
#     data: Dict[str, Any] = {
#         "event_id": 1,
#         "label": "タイトル",
#         "color": "色",
#     }
#     r = client.post("/api/tags/", json=data)
#     assert r.status_code == StatusCode.BadRequest


# def test_get_tag_list_by_event_id(client: TestClient, db: scoped_session) -> None:
#     event_id = 1
#     r: requests.Response = client.get(f"/api/tag/{event_id}")
#     assert r.status_code == StatusCode.OK


# def test_get_tag_list(client: TestClient, db: scoped_session) -> None:
#     r: requests.Response = client.get("/api/tags/")
#     assert r.status_code == StatusCode.OK


def test_get_tag_list_by_event_id(client: TestClient, db: scoped_session) -> None:
    event_id = 1
    r: requests.Response = client.get(f"/api/tags/{event_id}")
    assert r.status_code == StatusCode.OK


def test_get_tag_list_by_event_id_error(
    client: TestClient, db: scoped_session
) -> None:
    event_id = 100
    r: requests.Response = client.get(f"/api/tags/{event_id}")
    assert r.status_code == StatusCode.BadRequest


def test_get_tag(client: TestClient, db: scoped_session) -> None:
    tag_id = 1
    # event_id = 1
    r: requests.Response = client.get(f"/api/tags/{tag_id}")
    assert r.status_code == StatusCode.OK


def test_get_tag_error(client: TestClient, db: scoped_session) -> None:
    tag_id = 100
    # event_id = 1
    r: requests.Response = client.get(f"/api/tags/{tag_id}")
    assert r.status_code == StatusCode.BadRequest


def test_delete_tag(client: TestClient, db: scoped_session) -> None:
    tag_id = 1
    event_id = 1
    r: requests.Response = client.delete(f"/api/tags/{event_id}/{tag_id}")
    assert r.status_code == StatusCode.OK


def test_delete_tag_error_invalid_event(
    client: TestClient, db: scoped_session
) -> None:
    tag_id = 1
    event_id = 100
    r: requests.Response = client.delete(f"/api/tags/{event_id}/{tag_id}")
    assert r.status_code == StatusCode.NotFound


def test_delete_tag_error(client: TestClient, db: scoped_session) -> None:
    tag_id = 100
    event_id = 1
    r: requests.Response = client.delete(f"/api/tags/{event_id}/{tag_id}")
    assert r.status_code == StatusCode.BadRequest
