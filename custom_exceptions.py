class BankError(Exception):
    def __init__(self, message="Unknown Bank Error"):
        super().__init__()
        self.message = message

class NegativeMoneyError(BankError):
    def __init__(self, message="Negative Money Error"):
        super().__init__(message)

class WrongAccountNumberError(BankError):
    def __init__(self, message="Wrong Account Number Error"):
        super().__init__(message)

class AccountNotFound(BankError):
    def __init__(self, message="Account Not Found"):
        super().__init__(message)

class WrongActionError(BankError):
    def __init__(self, message="Wrong Action Error"):
        super().__init__(message)

class NotEnoughMoneyError(BankError):
    def __init__(self, message="Not Enough Money Error"):
        super().__init__(message)

class AccountAlreadyExists(BankError):
    def __init__(self, message="Account Already Exists"):
        super().__init__(message)