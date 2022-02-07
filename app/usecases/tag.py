import abc
from typing import Optional
import app.domains.entities.tag as entities


class ITagRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def create_tag(self, obj_in: entities.TagCreate) -> entities.Tag:
        raise NotImplementedError

    @abc.abstractmethod
    def get_tag_by_id(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        raise NotImplementedError

    @abc.abstractmethod
    def delete_tag(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        raise NotImplementedError


class TagUsecase:
    repo: ITagRepository

    def __init__(self, repo: ITagRepository) -> None:
        self.repo = repo

    def create_tag(self, obj_in: entities.TagCreate) -> entities.Tag:
        return self.repo.create_tag(obj_in=obj_in)

    def get_tag_by_id(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        return self.repo.get_tag_by_id(event_id=event_id, tag_id=tag_id)

    def delete_tag(self, event_id: int, tag_id: int) -> Optional[entities.Tag]:
        return self.repo.delete_tag(event_id=event_id, tag_id=tag_id)