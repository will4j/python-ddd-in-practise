from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from pydantic import BaseModel, ConfigDict

T = TypeVar('T')


class DomainObject(BaseModel):
    """Base class of all domain objects"""


class ValueObject(DomainObject, ABC):
    """Base class of all value objects"""

    model_config = ConfigDict(frozen=True)

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __hash__(self):
        pass


class EntityId(ValueObject, Generic[T]):
    """Base class of all domain entity id objects"""
    value: T

    def get_value(self) -> T:
        return self.value

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.get_value() == other.get_value()

    def __hash__(self):
        return hash(self.value)


class Entity(DomainObject):
    """Base class of all domain entity objects"""

    @abstractmethod
    def get_id(self) -> EntityId:
        pass


class AggregateRoot(Entity, ABC):
    """Base class of all aggregate root objects"""
    pass


class DomainService(ABC):
    """Base class of all domain services"""
    pass


class Command(DomainObject):
    """Base class of all domain commands"""


class DomainException(Exception):
    """Base exception of all domain exceptions"""
    pass
