
from bank_account import BankAccount

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {
            'account1': BankAccount(int_rate=0.02, balance=0),
            'account2': BankAccount(int_rate=0.03, balance=0)
        }


    def make_deposit(self, amount, account_key='account1'):
        if account_key not in self.accounts:
            print(f"Account {account_key} does not exist for user {self.name}.")
            return self
        self.accounts[account_key].deposit(amount)
        return self


    def make_withdrawal(self, amount, account_key='account1'):
        if account_key not in self.accounts:
            print(f"Account {account_key} does not exist for user {self.name}.")
            return self
        self.accounts[account_key].withdraw(amount)
        return self


    def display_user_balance(self):
        for account_key, account in self.accounts.items():
            print(f"User: {self.name}, Account: {account_key}, Balance: ${account.balance}")
        return self
    

user = User("Bilal", "bilal@gmail.com")

user.make_deposit(100)
user.make_deposit(200, 'account2')
user.make_withdrawal(50)
user.make_withdrawal(30, 'account2')
user.display_user_balance()