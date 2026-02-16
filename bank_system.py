from account import *

accounts = {}

def get_account():
    while True:
        try:
            account_number = input("Enter account number: ")
            if int(account_number) < 0:
                raise ValueError
            elif any(account.account_number==account_number for account in accounts):
                raise ValueError("WRONG ACCOUNT NUMBER!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                new_account = Account(account_number, input("Enter name: "), input("Enter balance: "))
                accounts[new_account.account_number]=new_account

            break
        finally:
            print("Invalid Account Number. try again")

while True:
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
            if not (action==7 or action==1):
                number = int(input("what is your account number? : "))
                account=accounts[number]
            if not action in range(1, 7):
                raise ValueError
            break
        except Exception:
            print("\nInvalid input. Try again.")

    match action:
        case 1:
            try:
                get_account()
            finally:
                pass
            break
        case 2:
            try:
                account.deposit(input("Enter amount to deposit: "))
            except ValueError as e:
                print(e.message)
            break

        case 3:
            try:
                account.withdraw(input("Enter amount to withdraw: "))
            except ValueError as e:
                print(e.message)
            break
        case 4:
            try:
                to=account[input("Enter an account to transfer")]
                account.transfer(to,input("Enter amount to deposit: "))
            except KeyError:
                print("\naccount doesnt exist. Guten morgen.")
            finally:
                pass
            break
        case 5:
            try:
                print(f"The balance is {account.balance}")
            finally:
                pass
            break
        case 6:
            try:
                account.print_actions()
            finally:
                pass
            break
        case 7:
            try:
                print("Goodbye")
                break
            finally:
                pass
            break










