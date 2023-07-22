from abc import ABC
from abc import abstractmethod

from domain.model.piggy_bank import PiggyBank


class PiggyBankRepository(ABC):

    @abstractmethod
    def get(self) -> PiggyBank:
        pass

    @abstractmethod
    def save(self, piggy_bank: PiggyBank):
        pass
