from application.piggy_bank_service import PiggyBankServie
from infrastructure.adapters.memory.memory_piggy_bank_persistence import MemoryPiggyBankPersistence


def mock_piggy_bank_service(balance) -> PiggyBankServie:
    piggy_bank_repository = MemoryPiggyBankPersistence(balance)
    piggy_bank_service = PiggyBankServie(piggy_bank_repository)
    return piggy_bank_service


def test_check_balance():
    piggy_bank_service = mock_piggy_bank_service(10.0)
    assert piggy_bank_service.balance() == 10.0


def test_deposit():
    piggy_bank_service = mock_piggy_bank_service(10.0)
    piggy_bank_service.deposit(1.5)
    assert piggy_bank_service.balance() == 11.5
