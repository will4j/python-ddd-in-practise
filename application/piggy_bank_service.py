from application.ports.input.piggy_bank_use_case import CheckPiggyBankUseCase
from application.ports.input.piggy_bank_use_case import SavePiggyBankUseCase
from domain.repository.piggy_bank_repository import PiggyBankRepository


class PiggyBankServie(CheckPiggyBankUseCase, SavePiggyBankUseCase):

    def __init__(self, piggy_bank_repository: PiggyBankRepository):
        self.piggy_bank_repository = piggy_bank_repository

    def balance(self):
        pass

    def deposit(self, amount):
        pass
