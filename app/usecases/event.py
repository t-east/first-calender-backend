import abc
from typing import Any, Dict, Optional, Union

import app.domains.entities as entities


class IEventRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def read(self, id: int, user_id: int) -> Optional[entities.Event]:
        raise NotImplementedError

    @abc.abstractmethod
    def create(self, obj_in: entities.EventCreate) -> entities.Event:
        raise NotImplementedError

    @abc.abstractmethod
    def update(
        self, id: int, user_id: int, obj_in: Union[entities.EventUpdate, Dict[str, Any]]
    ) -> Optional[entities.Event]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, id: int, user_id: int) -> Optional[entities.Event]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_list(self, user_id: int) -> entities.ListEventsResponse:
        raise NotImplementedError

    @abc.abstractclassmethod
    def get_tag(self, ):
        raise NotImplementedError


class EventUsecase:
    repo: IEventRepository

    def __init__(self, repo: IEventRepository) -> None:
        self.repo = repo

    def read(self, id: int, user_id: int) -> Optional[entities.Event]:
        return self.repo.read(id=id, user_id=user_id)

    def create(self, obj_in: entities.EventCreate) -> entities.Event:
        return self.repo.create(obj_in=obj_in)

    def update(
        self, id: int, user_id: int, obj_in: Union[entities.EventUpdate, Dict[str, Any]]
    ) -> Optional[entities.Event]:
        return self.repo.update(id=id, user_id=user_id, obj_in=obj_in)

    def delete(self, id: int, user_id: int) -> Optional[entities.Event]:
        return self.repo.delete(id=id, user_id=user_id)

    def get_list(self, user_id: int) -> entities.ListEventsResponse:
        return self.repo.get_list(user_id=user_id)

    def get_tag(self, user_id: int, id: int, tag_id: int) -> entities:
        return self.repo.get_tag(user_id=user_id, id=id, tag_id=tag_id)

    # def create_tag(self, user_id: int, id: int, obj_in: Union[entities.])
