import abc
from typing import Any, Dict, Optional, Union

import app.domains.entities as entities


class IUserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, id: int) -> Optional[entities.User]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_email(self, email: str) -> Optional[entities.User]:
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

    @abc.abstractmethod
    def authenticate(self, email: str, password: str) -> Optional[entities.User]:
        raise NotImplementedError


class UserUsecase:
    repo: IUserRepository

    def __init__(self, repo: IUserRepository) -> None:
        self.repo = repo

    def get(self, id: int) -> Optional[entities.User]:
        return self.repo.get(id=id)

    def get_by_email(self, email: str) -> Optional[entities.User]:
        return self.repo.get_by_email(email=email)

    def create(self, obj_in: entities.UserCreate) -> entities.User:
        return self.repo.create(obj_in=obj_in)

    def update(
        self, id: int, obj_in: Union[entities.UserUpdate, Dict[str, Any]]
    ) -> Optional[entities.User]:
        return self.repo.update(id=id, obj_in=obj_in)

    def delete(self, id: int) -> Optional[entities.User]:
        return self.repo.delete(id=id)

    def authenticate(self, email: str, password: str) -> Optional[entities.User]:
        return self.repo.authenticate(email=email, password=password)
