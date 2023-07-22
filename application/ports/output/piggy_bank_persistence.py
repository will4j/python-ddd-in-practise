from abc import ABC

from domain.repository.piggy_bank_repository import PiggyBankRepository


class PiggyBankPersistence(PiggyBankRepository, ABC):
    pass
