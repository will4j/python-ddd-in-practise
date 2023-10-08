from application.ports.input.piggy_bank_use_case import CheckPiggyBankUseCase
from application.ports.input.piggy_bank_use_case import SavePiggyBankUseCase
from domain.piggy_bank.repository import PiggyBankRepository


class PiggyBankServie(CheckPiggyBankUseCase, SavePiggyBankUseCase):

    def __init__(self, piggy_bank_repository: PiggyBankRepository):
        self.piggy_bank_repository = piggy_bank_repository

    def balance(self) -> float:
        piggy_bank = self.piggy_bank_repository.get()
        return piggy_bank.check_balance()

    def deposit(self, amount: float) -> None:
        piggy_bank = self.piggy_bank_repository.get()
        piggy_bank.deposit(amount)
        self.piggy_bank_repository.save(piggy_bank)
