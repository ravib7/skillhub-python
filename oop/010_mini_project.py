# create a class called Account
# add parameterized constuctor with name and amount
# method 1 credit 2 debit 3 check balance

class Account:
    def __init__(self, name, amount):
        self._name = name
        self.balance = amount

    def debit(self, amount):
        self.balance -= amount
        print(f"Account Debittd With Amount {amount}")

    def credit(self, amount):
        self.balance += amount
        print(f"Account Credited With Amount {amount}")

    def check_balance(self):
        return self.balance

class SavingsAccount(Account):
    def add_interest(self):
        self.balance += self.balance * 0.05


cust1 = SavingsAccount("Ross Doe", 100)
print()

# cust1.add_interest()
# print(cust1.check_balance())

# customer1 = Account("John Doe", 100)
# print(customer1.check_balance())
# customer1.debit(50)
# print(customer1.check_balance())
# customer1.credit(50)
# print(customer1.check_balance())
