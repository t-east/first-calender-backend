import abc
from typing import Optional
import app.domains.entities.tag as entities


class ITagRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, obj_in: entities.TagCreate) -> entities.Tag:
        raise NotImplementedError

    @abc.abstractmethod
    def get_by_id(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_list_by_id(self, event_id: int) -> Optional[entities.ListTagsResponse]:
        raise NotImplementedError

class TagUsecase:
    repo: ITagRepository

    def __init__(self, repo: ITagRepository) -> None:
        self.repo = repo

    def create(self, obj_in: entities.TagCreate) -> entities.Tag:
        return self.repo.create(obj_in=obj_in)

    def get_by_id(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        return self.repo.get_by_id(event_id=event_id, tag_id=tag_id)

    def delete(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        return self.repo.delete(event_id=event_id, tag_id=tag_id)

    def get_list_by_id(self, event_id: int) -> Optional[entities.ListTagsResponse]:
        return self.repo.get_list_by_id(event_id=event_id)