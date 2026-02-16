from account import *

accounts = {}

def get_account():
    while True:
        try:
            account_number = input("Enter account number: ")
            if int(account_number) < 0:
                raise ValueError
            
            break
        finally:
            print("Invalid Account Number. try again")






while True:
    while True:
        print("\nChoose an action:"
              "\n(1) Create new account"
              "\n(2) Deposit money"
              "\n(3) Withdraw money"
              "\n(4) Transfer"
              "\n(5) Show balance"
              "\n(6) Show past actions"
              "\n(7) Exit")
        try:
            action = int(input("\nChoose an action: "))
            if not action in range(1, 7):
                raise ValueError
            break
        except Exception:
            print("\nInvalid input. Try again.")
    match action:
        case 1:
            try:
                account = get_account()










