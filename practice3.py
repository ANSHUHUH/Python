class BankAccount:

    account_number = 1000100

    def __init__(self, owner_name, balance):
        self.owner_name = owner_name
        self.balance = balance
        self.account_number += 1

    def deposit(self, money):
        self.balance += money
        print("Balance:", self.balance)

    def withdraw(self, money):
        self.balance -= money
        print("Balance:", self.balance)

    def check_balance(self):
        print("Balance:", self.balance)


acc = BankAccount("Anshu", 1000)

acc.deposit(1000)
acc.withdraw(500)
acc.check_balance()