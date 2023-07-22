from abc import ABC
from abc import abstractmethod


class CheckPiggyBankUseCase(ABC):

    @abstractmethod
    def balance(self):
        """Check balance of the piggy bank.

        Returns:
            float: balance of the piggy bank balance.
        """
        pass


class SavePiggyBankUseCase(ABC):

    @abstractmethod
    def deposit(self, amount):
        """Put money into the piggy bank.

        Args:
             amount: money to put
        Returns:
            bool: success or failed
        """
        pass
