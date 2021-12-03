from typing import Any, Dict, Optional, Union

# from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

import app.domains.entities as entities
import app.drivers.rdb.models as models

# from app.drivers.security import get_password_hash, verify_password
# from app.drivers.sqlalchemy_to_pydantic import sqlalchemy_to_pydantic
import app.usecases as usecases

# ここで記述処理は，型の変換と最小限のエラー処理．メインロジックはusecaseが担当するのであまり余計な事は書かない．
class SQLEventRepository(usecases.IEventRepository):
    def __init__(self, db: Session) -> None:
        pass

    def _get_by_id(self, id: int) -> Optional[models.Event]:
        pass  # このクラス内でのみ使うid検索関数．modelの型からentitiesの型にする前準備の関数として切り離しておく

    def get(self, id: int, user_int: int) -> Optional[entities.Event]:
        pass  # _get_by_idで得たmodelsのuser_idと入力したuser_idを比較して正しければentities.Eventを返す

    def create(self, obj_in: entities.EventCreate) -> entities.Event:
        pass  # イベント作成の処理で入力したentities.EventCreateの型をmodelsの型にしてdbに保存．その後取り出したものをentities.Eventになおして出力

    def update(
        self, id: int, user_id: int, obj_in: Union[entities.EventUpdate, Dict[str, Any]]
    ) -> Optional[entities.Event]:
        pass  # _get_by_idで得たmodelsのuser_idと入力したuser_idを比較して正しければ，入力値を元にdbを更新，その後取り出したものをentities.Eventになおして出力

    def delete(self, id: int, user_id: int) -> Optional[entities.Event]:
        pass  # 削除の前に_get_by_idで得たmodelsのuser_idと入力したuser_idを比較して正しい事を確認，その後入力されたidのDBを削除，削除するデータをentities.Eventにして出力

    def get_list(self, user_id: int) -> entities.ListEventsResponse:
        pass  # 入力したuser_idに当てはまるeventを全件取得．その後entities.ListEventsResponseの形で出力
