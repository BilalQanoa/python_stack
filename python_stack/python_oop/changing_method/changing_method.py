class User:
    def __init__ (self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    
    def make_deposit(self, amount):
        self.balance += amount
        return self
    
    def make_withdrawal(self, amount):
        if self.balance < amount:
            print("Your balance is less than the amount you want to withdraw.")
        else:
            self.balance -= amount
        return self
    
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.balance}")
        return self
    
    def transfer_money(self, other_user, amount):
        if self.balance < amount:
            print("Your balance is less than the amount you want to transfer.")
        else:
            self.make_withdrawal(amount)
            other_user.make_deposit(amount)
        return self
    

user1 = User("Bilal", "bilal@gmail.com")
user2 = User("Ahmed", "ahmed@gmail.com")
user3 = User("Khaled", "khaled@gmail.com")

# user 1
print("User 1:")
user1.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(100).display_user_balance()

# user 2
print("User 2:")
user2.make_deposit(100).make_deposit(200).make_withdrawal(100).display_user_balance()

# user 3
print("User 3:")
user3.make_deposit(200).make_withdrawal(100).make_withdrawal(100).make_withdrawal(100)
user3.display_user_balance()


user1.transfer_money(user3, 100)
print("User 1 after transfer:")
user1.display_user_balance()
print("User 3 after receiving transfer:")
user3.display_user_balance()