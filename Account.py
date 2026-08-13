class Account:
    def __init__(self, balance, accNo):
        self.balance = balance
        self.accNo = accNo

    def debit(self, amount):
        if self.balance >= 0:
            self.balance -= amount
            print("Rs", amount, "is debited!")
            print("Your balance is now", self.get_balance())
        else:
            print("Balance not enough!")

    def credit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Rs", amount, "is credited!")
            print("Your balance is now", self.get_balance())
        else:
            print("Invalid amount!")

    def get_balance(self):
        return self.balance

user = Account(60000, 1234) 
user.credit(5000)
user.debit(30000)