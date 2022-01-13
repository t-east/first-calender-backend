from typing import Any, Dict, Optional, Union

# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.drivers.models.user as models
import hashlib
from fastapi import HTTPException
from datetime import datetime

# from pydantic import constr


# from app.drivers.security import get_password_hash, verify_password
# from app.drivers.sqlalchemy_to_pydantic import sqlalchemy_to_pydantic
import app.usecases as usecases


# ここで記述処理は，型の変換と最小限のエラー処理．メインロジックはusecaseが担当するのであまり余計な事は書かない．
class SQLUserRepository(usecases.IUserRepository):
    def __init__(self, db: Session) -> None:
        self.db = db

    def _get_by_id(self, id: int) -> Optional[models.User]:
        get_user_model = (
            self.db.query(models.User).filter(models.User.user_id == id).first()
        )
        if not get_user_model:
            return None
        return get_user_model

    def read(self, id: int) -> Optional[entities.User]:
        get_user_by_id = self._get_by_id(id)
        if not get_user_by_id:
            raise HTTPException(status_code=404, detail="指定されたユーザーは存在しません")
        read_user = entities.User.from_orm(get_user_by_id)
        return read_user

    def _get_by_email(self, email: str) -> Optional[models.User]:
        get_user_model = (
            self.db.query(models.User).filter(models.User.email == email).first()
        )
        if not get_user_model:
            return None
        return get_user_model

    def create(self, obj_in: entities.UserCreate) -> entities.User:
        db_user = models.User(
            user_name=obj_in.user_name,
            email=obj_in.email,
            birthday=obj_in.birthday,
            password_hash=hashlib.sha256(obj_in.password.encode()).hexdigest(),
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        db_user_entities = entities.User.from_orm(db_user)
        return db_user_entities

    def update(
        self, id: int, obj_in: Union[entities.UserUpdate, Dict[str, Any]]
    ) -> Optional[entities.User]:
        get_user_model = self._get_by_id(id)
        if not get_user_model:
            raise HTTPException(status_code=404, detail="指定されたユーザーは存在しません")

        for var, value in vars(obj_in).items():
            setattr(get_user_model, var, value) if value else None

        get_user_model.updated_at = datetime.utcnow()
        self.db.add(get_user_model)
        self.db.commit()
        self.db.refresh(get_user_model)
        get_user_model_entities = entities.User.from_orm(get_user_model)
        return get_user_model_entities

    def delete(self, id: int) -> Optional[entities.User]:
        delete_user_model = models.User.delete().where(models.User.user_id == id)
        if not delete_user_model:
            raise HTTPException(status_code=404, detail="指定されたユーザーは存在しないか，既に削除されています")
        delete_user_entities = entities.User.from_orm(delete_user_model)
        self.db.delete_user_model()
        return delete_user_entities

    def authenticate(self, auth_in: entities.UserAuth) -> Optional[entities.User]:
        pass
        # 入力されたメールアドレス，パスワードを用いてDBの値と一致しているか確認する．
        # _get_by_emailを使って得たhashedpassとpasswordをハッシュ化したものを比較して正しければentities.Userを出力
