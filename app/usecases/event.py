import abc
from typing import Any, Dict, Optional, Union
import app.domains.entities as entities


class IEventRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, obj_in: entities.EventCreate) -> entities.Event:
        raise NotImplementedError

    @abc.abstractmethod
    def update(
        self,
        event_id: int,
        user_id: int,
        obj_in: Union[entities.EventUpdate, Dict[str, Any]],
    ) -> Optional[entities.Event]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, event_id: int, user_id: int) -> Optional[entities.Event]:
        raise NotImplementedError

    @abc.abstractmethod
    def get_list(self) -> entities.ListEventsResponse:
        raise NotImplementedError

    @abc.abstractmethod
    def get_list_by_id(self, user_id: int) -> entities.ListEventsResponse:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, event_id: int, user_id: int) -> Optional[entities.Event]:
        raise NotImplementedError


class EventUsecase:
    repo: IEventRepository

    def __init__(self, repo: IEventRepository) -> None:
        self.repo = repo

    def create(self, obj_in: entities.EventCreate) -> entities.Event:
        return self.repo.create(obj_in=obj_in)

    def update(
        self,
        event_id: int,
        user_id: int,
        obj_in: Union[entities.EventUpdate, Dict[str, Any]],
    ) -> Optional[entities.Event]:
        return self.repo.update(event_id=event_id, user_id=user_id, obj_in=obj_in)

    def delete(self, event_id: int, user_id: int) -> Optional[entities.Event]:
        return self.repo.delete(event_id=event_id, user_id=user_id)

    def get_list(self) -> entities.ListEventsResponse:
        return self.repo.get_list()

    def get_list_by_id(self, user_id: int) -> entities.ListEventsResponse:
        return self.repo.get_list_by_id(user_id=user_id)

    def get_by_id(self, event_id: int, user_id: int) -> Optional[entities.Event]:
        return self.repo.get_by_id(event_id=event_id, user_id=user_id)
