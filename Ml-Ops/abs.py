class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance

    def deposite(self, amount):
        if amount >0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive")
    def withdraw(self,amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
    
    def get_balance(self):
        return self.__balance
acc = Account("Ram", 1000)
acc.deposite(500)
print("Current Balance:", acc.get_balance())