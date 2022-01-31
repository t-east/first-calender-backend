from typing import Any, Dict, Optional, Union, List

# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.drivers.rdb.models.event as models
import app.drivers.rdb.models.user as user_models
from fastapi import HTTPException
import datetime

import app.usecases as usecases


# ここで記述処理は，型の変換と最小限のエラー処理．メインロジックはusecaseが担当するのであまり余計な事は書かない．
class SQLEventRepository(usecases.IEventRepository):
    def __init__(self, db: Session) -> None:
        self.db: Session = db
        self.model = models.Event
        self.user_model = user_models.User

    def _validate_date(self, from_date: datetime.date, to_date: datetime.date) -> bool:
        return to_date < from_date

    def _find_user(self, user_id: int) -> bool:
        user = (
            self.db.query(self.user_model)
            .filter(self.user_model.user_id == user_id)
            .first()
        )
        if not user:
            return False
        return True

    def _find_event(self, event_id: int) -> Optional[models.Event]:
        event = (
            self.db.query(self.model).filter(self.model.event_id == event_id).first()
        )
        return event

    def _get_list_by_id(self, user_id: int) -> Optional[models.Event]:
        get_event_model = (
            self.db.query(self.model).filter(self.model.user_id == user_id).all()
        )
        if not get_event_model:
            return None
        return get_event_model

    def create(self, obj_in: entities.EventCreate) -> entities.Event:
        db_event = models.Event(
            title=obj_in.title,
            user_id=obj_in.user_id,
            description_text=obj_in.description_text,
            from_date=obj_in.from_date,
            is_all_day=obj_in.is_all_day,
            to_date=obj_in.to_date,
            created_at=datetime.datetime.now(),
        )
        if self._validate_date(obj_in.from_date, obj_in.to_date):
            raise HTTPException(status_code=400, detail="invalid date")
        self.db.add(db_event)
        self.db.commit()
        self.db.refresh(db_event)
        self.db.flush()
        read_entities = entities.Event.from_orm(db_event)
        return read_entities

    def update(
        self,
        event_id: int,
        user_id: int,
        obj_in: Union[entities.EventUpdate, Dict[str, Any]],
    ) -> Optional[entities.Event]:
        if not self._find_user(user_id):
            raise HTTPException(status_code=401, detail="指定されたユーザーは存在しません")
        get_event_model = self._find_event(event_id)
        if not get_event_model:
            raise HTTPException(status_code=404, detail="指定されたイベントは存在しません")

        for var, value in vars(obj_in).items():
            setattr(get_event_model, var, value) if value else None

        get_event_model.updated_at = datetime.datetime.now()
        self.db.add(get_event_model)
        self.db.commit()
        self.db.refresh(get_event_model)
        get_event_model_entities = entities.Event.from_orm(get_event_model)
        return get_event_model_entities

    def delete(self, event_id: int, user_id: int) -> Optional[entities.Event]:
        if not self._find_user(user_id=user_id):
            raise HTTPException(status_code=401, detail="指定されたユーザーは存在しません")
        event_in_db = self._find_event(event_id=event_id)
        if not event_in_db:
            raise HTTPException(status_code=400, detail="指定されたイベントは存在しません")
        self.db.delete(event_in_db)
        deleted_event = entities.Event.from_orm(event_in_db)
        return deleted_event
        # 削除の前に_get_by_idで得たmodelsのuser_idと入力したuser_idを比較して正しい事を確認?

    def get_list(self) -> entities.ListEventsResponse:
        events_in_db = self.db.query(self.model).all()
        events: List[entities.Event] = [
            entities.Event.from_orm(event) for event in events_in_db
        ]
        total: int = self.db.query(self.model).count()
        return entities.ListEventsResponse(total=total, events=events)

    def get_list_by_id(self, user_id: int) -> entities.ListEventsResponse:
        if not self._find_user(user_id=user_id):
            raise HTTPException(status_code=400, detail="指定されたユーザーは存在しません")
        query = self.db.query(self.model).filter(self.model.user_id == user_id)
        events_in_db = query.all()
        events: List[entities.Event] = [
            entities.Event.from_orm(event) for event in events_in_db
        ]
        total: int = query.count()
        return entities.ListEventsResponse(total=total, events=events)

    def get_by_id(self, event_id: int, user_id: int) -> Optional[entities.Event]:
        if not self._find_user(user_id=user_id):
            raise HTTPException(status_code=401, detail="指定されたユーザーは存在しません")
        get_event_model = self._find_event(event_id=event_id)
        if not get_event_model:
            raise HTTPException(status_code=404, detail="指定されたイベントは存在しません")
        query = (
            self.db.query(self.model)
            .filter(self.model.user_id == user_id, self.model.event_id == event_id)
            .first()
        )
        event = entities.Event.from_orm(query)
        return event
