from application.ports.output.piggy_bank_persistence import PiggyBankPersistence
from domain.model.piggy_bank import PiggyBank


class MemoryPiggyBankPersistence(PiggyBankPersistence):
    def __init__(self, balance):
        self.balance = balance

    def get(self) -> PiggyBank:
        pass

    def save(self, piggy_bank: PiggyBank):
        pass
