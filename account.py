from datetime import datetime
from custom_exceptions import *

time = lambda: datetime.now().strftime("%Y - %m- %d %H:%M")

class Account:
    def __init__(self, account_number, owner_name, balance = 0, actions = []):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.actions = actions

        actions.append(f"Created account at {time()}")

    def deposit(self, amount):
        if amount < 0:
            raise NegativeMoneyError("Deposit amount cannot be negative")
        self.balance += amount
        self.actions.append(f"deposit {amount} at {time()}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise NotEnoughMoneyError("Not enough money to withdraw")
        if amount < 0:
            raise NegativeMoneyError("Withdraw amount cannot be negative")
        self.balance -= amount
        self.actions.append(f"withdraw {amount} at {time()}")

    def transfer(self, to , amount):
        if amount < 0:
            raise NegativeMoneyError("Transfer amount cannot be negative")
        if amount > self.balance:
            raise NotEnoughMoneyError("Transfer amount cannot be greater than balance")
        to.balance += amount
        self.balance -= amount
        self.actions.append(f"transfer {amount} to account no. {to.account_number} at {time()}")

    def print_actions(self):
        for action in self.actions:
            print(action)

