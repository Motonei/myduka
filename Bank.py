
from datetime import date

class BankAccount:
    def __init__(self, account_number, balance, owner_name, date_opened):
        self.account_number = account_number
        self.balance = balance
        self.owner_name = owner_name
        self.date_opened = date_opened
        self.is_closed = False

    def deposit(self, amount):
        if self.is_closed:
            print("Account is closed. Cannot deposit.")
            return
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if self.is_closed:
            print("Account is closed. Cannot withdraw.")
            return
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: ${self.balance:.2f}")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def check_balance(self):
        if self.is_closed:
            print("Account is closed.")
            return
        print(f"Current balance for {self.owner_name}: ${self.balance:.2f}")

    def display_info(self):
        status = "Closed" if self.is_closed else "Active"
        print(f"--- Account Info ---")
        print(f"Owner:          {self.owner_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance:        ${self.balance:.2f}")
        print(f"Date Opened:    {self.date_opened}")
        print(f"Status:         {status}")
        

    def close_account(self):
        if self.is_closed:
            print("Account is already closed.")
            return
        self.is_closed = True
        print(f"Account {self.account_number} for {self.owner_name} has been closed.")




account1 = BankAccount("ACC-1001", 1000.00, "Alice Wanjiru", date(2024, 1, 15))
account2 = BankAccount("ACC-1002", 500.00, "Brian Otieno", date(2025, 3, 22))


account1.display_info()
account1.deposit(250.00)
account1.withdraw(100.00)
account1.check_balance()
account1.close_account()
account1.deposit(50.00)   

print()
account2.display_info()
account2.deposit(300.00)
account2.withdraw(900.00) 
account2.withdraw(200.00)
account2.check_balance()
account2.close_account()