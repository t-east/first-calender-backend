from typing import Any, Dict, Optional, Union

# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.drivers.rdb.models as models

# from app.drivers.security import get_password_hash, verify_password
# from app.drivers.sqlalchemy_to_pydantic import sqlalchemy_to_pydantic
import app.usecases as usecases

# ここで記述処理は，型の変換と最小限のエラー処理．メインロジックはusecaseが担当するのであまり余計な事は書かない．
class SQLUserRepository(usecases.IUserRepository):
    def __init__(self, db: Session) -> None:
        pass

    def _get(self, id: int) -> Optional[models.User]:
        pass  # このクラス内でのみ使うid検索関数．modelの型からentitiesの型にする前準備の関数として切り離しておく

    def get(self, id: int) -> Optional[entities.User]:
        pass  # _getで得たmodelsをentities.Userで出力

    def _get_email(self, email: str) -> Optional[models.User]:
        pass  # このクラス内でのみ使うメールアドレス検索関数．modelの型からentitiesの型にする前準備の関数として切り離しておく

    def create(self, obj_in: entities.UserCreate) -> entities.User:
        pass  # ユーザ登録の処理で入力したentities.UserCreateの型をmodelsの型にしてdbに保存．その後取り出したものをentities.Userになおして出力

    def update(
        self, id: int, obj_in: Union[entities.UserUpdate, Dict[str, Any]]
    ) -> Optional[entities.User]:
        pass  # idと変更内容を含むentities.UserUpdateを用いて，DBを更新，entities.UserUpdateになおしてreturn

    def delete(self, id: int) -> Optional[entities.User]:
        pass  # 入力されたidのDBを削除，削除するデータをentities.Userにして出力

    def authenticate(self, auth_in: entities.UserAuth) -> Optional[entities.User]:
        pass
        # 入力されたメールアドレス，パスワードを用いてDBの値と一致しているか確認する．
        # _get_by_emailを使って得たhashedpassとpasswordをハッシュ化したものを比較して正しければentities.Userを出力
