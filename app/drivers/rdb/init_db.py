from sqlalchemy.orm import Session
from typing import Any, Dict, List

import app.drivers.api.deps as deps
import app.domains.entities as entities


def create_user(db: Session, data: dict) -> None:
    obj_in = entities.UserCreate(**data)
    uu = deps.get_user_usecase(db)
    uu.create(obj_in)


def create_event(db: Session, data: dict) -> None:
    obj_in = entities.EventCreate(**data)
    eu = deps.get_event_usecase(db)
    eu.create(obj_in)


def init_db(db: Session, fixtures: List[Dict[str, Any]]) -> None:
    for data in fixtures:
        eval(f"create_{data['model']}")(db, data["fields"])
