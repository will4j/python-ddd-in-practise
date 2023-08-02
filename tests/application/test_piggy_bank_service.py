import pytest

from infrastructure.adapters.memory.memory_piggy_bank_persistence import MemoryPiggyBankPersistence
from infrastructure.factory.di.piggy_bank_container import PiggyBankContainer


@pytest.fixture()
def container() -> PiggyBankContainer:
    container = PiggyBankContainer()
    container.piggy_bank_repository.override(MemoryPiggyBankPersistence(10.0))
    yield container
    container.piggy_bank_service.reset()


def test_check_balance(container):
    piggy_bank_service = container.piggy_bank_service()
    assert piggy_bank_service.balance() == 10.0


def test_deposit(container):
    piggy_bank_service = container.piggy_bank_service()
    piggy_bank_service.deposit(1.5)
    assert piggy_bank_service.balance() == 11.5
