from dependency_injector import containers
from dependency_injector import providers

from application.piggy_bank_service import PiggyBankServie
from infrastructure.adapters.memory.memory_piggy_bank_persistence import MemoryPiggyBankPersistence
from settings import CONFIG_FILE


class PiggyBankContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(packages=["infrastructure.adapters.rest.endpoints"])

    config = providers.Configuration(yaml_files=[CONFIG_FILE])

    piggy_bank_repository = providers.Singleton(MemoryPiggyBankPersistence,
                                                balance=0.0)

    piggy_bank_service = providers.Singleton(PiggyBankServie,
                                             piggy_bank_repository=piggy_bank_repository)
