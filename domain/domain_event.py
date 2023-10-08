from abc import ABC, abstractmethod
from datetime import datetime
from typing import TypeVar, Generic, Type, Set

from domain.domain_objects import DomainObject

T = TypeVar('T')


class DomainEvent(DomainObject, ABC):
    """Base class of all domain events"""

    @abstractmethod
    def occurred_on(self) -> datetime:
        """事件发生时间"""
        pass


class DomainEventSubscriber(ABC, Generic[T]):
    @abstractmethod
    def handle_event(self, event: T) -> None:
        pass

    @abstractmethod
    def subscribed_to_event_type(self) -> Type[T]:
        pass

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.__class__ == other.__class__

    def __hash__(self):
        return hash(self.__class__)


class DomainEventPublisher:
    _shared_borg_state = {}

    def __init__(self):
        if not hasattr(self, "subscribers"):
            self.subscribers: Set[DomainEventSubscriber] = set()
        if not hasattr(self, "publishing"):
            self.publishing: bool = False

    def __new__(cls, *args, **kwargs):
        obj = super(DomainEventPublisher, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_borg_state
        return obj

    @classmethod
    def instance(cls) -> "DomainEventPublisher":
        return cls()

    def publish(self, event: DomainEvent) -> None:
        if self.publishing:
            return
        try:
            self.publishing = True
            for subscriber in self.subscribers:
                if isinstance(event, subscriber.subscribed_to_event_type()):
                    subscriber.handle_event(event)
        finally:
            self.publishing = False

    def subscribe(self, subscriber: DomainEventSubscriber):
        if self.publishing:
            return
        self.subscribers.add(subscriber)
