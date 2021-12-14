from typing import Any, Dict, Optional, Union

# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.domains.entities as entities
# from app.domains.entities import user
# import app.drivers.models as models
import app.drivers.models.event as models
from fastapi import HTTPException
from datetime import datetime

# from app.drivers.security import get_password_hash, verify_password
# from app.drivers.sqlalchemy_to_pydantic import sqlalchemy_to_pydantic
import app.usecases as usecases


# ここで記述処理は，型の変換と最小限のエラー処理．メインロジックはusecaseが担当するのであまり余計な事は書かない．
class SQLEventRepository(usecases.IEventRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def _get_by_id(self, id: int, user_id: int) -> Optional[models.Event]:
        get_event_model = (
            self.db.query(models.Event)
            .filter(models.Event.event_id == id and models.Event.user_id == user_id)
            .first()
        )
        if not get_event_model:
            return None
        return get_event_model

    def read(self, id: int, user_id: int) -> Optional[entities.Event]:
        get_event_by_id = self._get_by_id(id, user_id)
        if not get_event_by_id:
            raise HTTPException(status_code=404, detail="指定されたユーザーは存在しません")
        read_event = entities.Event.from_orm(get_event_by_id)
        return read_event

    def create(self, obj_in: entities.EventCreate) -> entities.Event:
        db_event = models.Event(
            event_title=obj_in.title,
            description=obj_in.description,
            begin_date=obj_in.begin_date,
            is_all_day=obj_in.is_all_day,
            end_date=obj_in.end_date,
            color=obj_in.color,
        )
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        db_event_entities = entities.Event.from_orm(db_event)
        return db_event_entities

    def update(
        self, id: int, user_id: int, obj_in: Union[entities.EventUpdate, Dict[str, Any]]
    ) -> Optional[entities.Event]:
        get_event_model = self._get_by_id(id, user_id)
        if not get_event_model:
            raise HTTPException(status_code=404, detail="指定されたユーザーは存在しません")

        for var, value in vars(obj_in).items():
            setattr(get_event_model, var, value) if value else None

        get_event_model.updated_at = datetime.utcnow()
        self.db.add(get_event_model)
        self.db.commit()
        self.db.refresh(get_event_model)
        get_event_model_entities = entities.Event.from_orm(get_event_model)
        return get_event_model_entities

    def delete(self, id: int, user_id: int) -> Optional[entities.Event]:
        delete_event_model = models.Event.delete().where(
            models.Event.event_id == id and models.Event.user_id == user_id
        )
        if not delete_event_model:
            raise HTTPException(status_code=404, detail="指定されたユーザーは存在しないか，既に削除されています")
        delete_event_entities = entities.Event.from_orm(delete_event_model)
        self.db.delete_event_model()
        return delete_event_entities
        # 削除の前に_get_by_idで得たmodelsのuser_idと入力したuser_idを比較して正しい事を確認?

    def get_list(self, user_id: int) -> entities.ListEventsResponse:
        get_all_user_events = (
            self.db.query(models.Event).filter(models.Event.user_id == user_id).all()
        )
        if not get_all_user_events:
            raise HTTPException(status_code=404, detail="指定されたユーザーは存在しないか，既に削除されています")
        get_all_user_events_entities = entities.ListEventsResponse.from_orm(
            get_all_user_events
        )
        return get_all_user_events_entities
