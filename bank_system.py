from account import *

accounts = {}

def get_account_number():
    while True:
        try:
            account_number = input("Enter account number: ")
            if int(account_number) < 0:
                raise WrongAccountNumberError("Account number cannot be negative")
            elif any(account.account_number==account_number for account in accounts):
                raise AccountAlreadyExists()
            else:
               return int(account_number)
        except BankError as e:
            print(e.message)
        except Exception:
            print("Unknown error")

def get_account():
    while True:
        try:
            account_number = input("Enter account number: ")
            if int(account_number) < 0:
                raise WrongAccountNumberError("Account number cannot be negative")
            elif any(account.account_number==account_number for account in accounts):
                raise AccountAlreadyExists()
            else:
                new_account = Account(account_number, input("Enter name: "), input("Enter balance: "))
                accounts[new_account.account_number]=new_account
            break
        except BankError as e:
            print(e.message)
        except Exception:
            print("Unknown error")

action = 1
while action in range(1,7):
    while True:
        print("\nAction:"
              "\n(1) Create new account"
              "\n(2) Deposit money"
              "\n(3) Withdraw money"
              "\n(4) Transfer"
              "\n(5) Show balance"
              "\n(6) Show past actions"
              "\n(7) Exit")
        try:
            action = int(input("\nChoose an action: "))
            if not action in range(1,7):
                raise WrongActionError("Wrong Action. Try again.")
            break
        except WrongActionError as e:
            print(e.message)
        except ValueError as e:
            print("Invalid Input. Try again.")
        finally:
            print("Unknown Error. Try again.")

    account = None
    if action != 1 and action != 7:
        account_number = get_account_number()
        account = accounts[account_number]

    match action:
        case 1: # -- Create Account --
            try:
                get_account()
            finally:
                pass
            break

        case 2: # -- Deposit --
            try:
                account.deposit(input("Enter amount to deposit: "))
            except BankError as e:
                print(e.message)
            break

        case 3: # -- Withdraw --
            try:
                account.withdraw(input("Enter amount to withdraw: "))
            except BankError as e:
                print(e.message)
            break
        case 4: # -- Transfer --
            try:
                to=account[get_account_number()]
                account.transfer(to,int(input("Enter amount to deposit: ")))
            except KeyError:
                print("\naccount doesnt exist. Guten morgen.")
            except BankError as e:
                print(e.message)
            break
        case 5: # -- Show Balance --
            print(f"The balance is {account.balance}")
            break
        case 6: # -- Show Past Actions --
            account.print_actions()
            break
        case 7: # -- Exit --
            print("Goodbye")
            exit()