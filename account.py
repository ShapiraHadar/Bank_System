class Account:
    def __init__(self, account_number, owner_name, balance = 0, actions = []):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance
        self.actions = actions

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount
        self.actions.append(f"deposit {amount}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Withdraw amount cannot be greater than balance")
        if amount < 0:
            raise ValueError("Withdraw amount cannot be negative")
        self.balance -= amount
        self.actions.append(f"withdraw {amount}")

    def transfer(self, to , amount):
        if amount < 0:
            raise ValueError("Transfer amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Transfer amount cannot be greater than balance")
        to.balance += amount
        self.balance -= amount
        self.actions.append(f"transfer {amount} to account no. {to.account_number}")

    def print_actions(self):
        for action in self.actions:
            print(action)

