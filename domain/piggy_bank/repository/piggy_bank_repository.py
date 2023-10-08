from abc import ABC
from abc import abstractmethod

from domain.piggy_bank.model import PiggyBank
from domain.piggy_bank.model import PiggyBankId


class PiggyBankRepository(ABC):

    @abstractmethod
    def next_id(self) -> PiggyBankId:
        pass

    @abstractmethod
    def get(self) -> PiggyBank:
        pass

    @abstractmethod
    def save(self, piggy_bank: PiggyBank):
        pass
