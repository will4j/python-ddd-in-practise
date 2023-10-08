from abc import ABC

from domain.piggy_bank.repository import PiggyBankRepository


class PiggyBankPersistence(PiggyBankRepository, ABC):
    pass
