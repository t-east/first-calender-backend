from typing import Optional


# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import app.domains.entities as entities
import app.drivers.rdb.models.event as event_models
import app.drivers.rdb.models.user as user_models
import app.drivers.rdb.models.tag as models
from fastapi import HTTPException
import datetime
import app.usecases as usecases


class SQLTagRepository(usecases.ITagRepository):
    def __init__(self, db: Session) -> None:
        self.db: Session = db
        self.event_model = event_models.Event
        self.user_model = user_models.User
        self.model = models.Tag

    def _find_tag(self, tag_id: int) -> Optional[models.Tag]:
        tag = self.db.query(self.model).filter(self.model.tag_id == tag_id).first()
        return tag

    def _find_event(self, event_id: int) -> Optional[event_models.Event]:
        event = (
            self.db.query(self.model).filter(self.model.event_id == event_id).first()
        )
        return event

    def create_tag(self, obj_in: entities.TagCreate) -> entities.Tag:
        db_tag = models.Tag(**obj_in.dict(), created_at=datetime.datetime.now())
        self.db.add(db_tag)
        self.db.commit()
        self.db.refresh(db_tag)
        return db_tag

    def get_tag_by_id(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        if not self._find_tag(tag_id=tag_id):
            raise HTTPException(status_code=401, detail="指定されたタグは存在しません")
        get_event_model = self._find_event(event_id=event_id)
        if not get_event_model:
            raise HTTPException(status_code=404, detail="指定されたイベントは存在しません")
        query = (
            self.db.query(self.model)
            .filter(self.model.tag_id == tag_id, self.model.event_id == event_id)
            .first()
        )
        event = entities.Tag.from_orm(query)
        return event

    def delete_tag(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        if not self._find_event(event_id=event_id):
            raise HTTPException(status_code=401, detail="指定されたイベントは存在しません")
        tag_in_db = self._find_tag(tag_id=tag_id)
        if not tag_in_db:
            raise HTTPException(status_code=400, detail="指定されたタグは存在しません")
        self.db.delete(tag_in_db)
        deleted_tag = entities.Tag.from_orm(tag_in_db)
        return deleted_tag
