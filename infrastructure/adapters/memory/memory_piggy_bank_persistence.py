from application.ports.output.piggy_bank_persistence import PiggyBankPersistence
from domain.piggy_bank.model import PiggyBank, PiggyBankId


class MemoryPiggyBankPersistence(PiggyBankPersistence):
    def __init__(self, balance: float):
        self.balance = balance

    def next_id(self) -> PiggyBankId:
        pass

    def get(self) -> PiggyBank:
        return PiggyBank(
            id=PiggyBankId(value="xxx"),
            balance=self.balance,
        )

    def save(self, piggy_bank: PiggyBank) -> None:
        self.balance = piggy_bank.check_balance()
