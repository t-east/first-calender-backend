import datetime

from sqlalchemy.orm import Session
from typing import Any, Dict, List

import app.drivers.api.deps as deps
import app.domains.entities as entities
import app.drivers.rdb.models as models


def create_user(db: Session, data: dict) -> None:
    obj_in = entities.UserCreate(**data)
    uu = deps.get_user_usecase(db)
    uu.create(obj_in)

    obj_in_db = db.query(models.User).get(data["id"])
    obj_in_db.created_at += datetime.timedelta(days=-2, hours=data["id"])
    db.add(obj_in_db)
    db.commit()
    db.refresh(obj_in_db)

def init_db(db: Session, fixtures: List[Dict[str, Any]]) -> None:
    for data in fixtures:
        eval(f"create_{data['model']}")(db, data["fields"])