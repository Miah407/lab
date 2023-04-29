class Account:

    def __init__(self, name: str) -> None:
        """
        Function to privately declare variables
        :param name: The name associated with the account
        """
        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        Function to determine if a deposit is valid and add it
        :param amount: Amount deposited into the account
        :return: If the deposit is valid or not (bool)
        """
        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """
        Function to determine if a withdraw is valid and subtract it
        :param amount: Amount withdrawn from the account
        :return: If the withdraw is valid or not (bool)
        """
        if 0 < amount < self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def get_balance(self) -> int:
        """
        Function to get the balance of the account
        :return: Account balance
        """
        return self.__account_balance

    def get_name(self) -> str:
        """
        Function to get the name for the account
        :return: Account name
        """
        return self.__account_name

