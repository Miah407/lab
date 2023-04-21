class Account:
    def __init__(self, name: str) -> None:
        self.account_name = name
        self.account_balance = 0

    def deposit(self, amount: float) -> bool:
        if amount > 0:
            self.account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        if 0 < amount < self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.account_balance

    def get_name(self):
        return self.account_name
