import abc
from typing import Any, Dict, Optional, Union

import app.domains.entities as entities


class IUserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, id: int) -> Optional[entities.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, obj_in: entities.UserCreate) -> entities.User:
        raise NotImplementedError

    @abc.abstractmethod
    def update(
        self, id: int, obj_in: Union[entities.UserUpdate, Dict[str, Any]]
    ) -> Optional[entities.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: int) -> Optional[entities.User]:
        raise NotImplementedError

    # @abc.abstractmethod
    # def authenticate(self, auth_in: entities.UserAuth) -> Optional[entities.User]:
    #     raise NotImplementedError


class UserUsecase:
    repo: IUserRepository

    def __init__(self, repo: IUserRepository) -> None:
        self.repo = repo

    def read(self, id: int) -> Optional[entities.User]:
        return self.repo.read(id=id)

    # 　他のユーザがメールアドレスを介してイベントを共有できる時にあったらいいかも
    # def get_by_email(self, email: str) -> Optional[str]:
    #     return self.repo.get_by_email(email=email)

    def create(self, obj_in: entities.UserCreate) -> entities.User:
        return self.repo.create(obj_in=obj_in)

    def update(
        self, id: int, obj_in: Union[entities.UserUpdate, Dict[str, Any]]
    ) -> Optional[entities.User]:
        return self.repo.update(id=id, obj_in=obj_in)

    def delete(self, id: int) -> Optional[entities.User]:
        return self.repo.delete(id=id)

    # def authenticate(self, auth_in: entities.UserAuth) -> Optional[entities.User]:
    #     return self.repo.authenticate(auth_in=auth_in)
