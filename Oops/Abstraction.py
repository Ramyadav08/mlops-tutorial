#hiding the implementation of class and only showing the essential part to the user is called abstraction

#encapsulation = wrapping up of data and methods into a single unit is called encapsulation
# __name : private attribute
# _name : protected attribute
# name : public attribute
# def __hello(): private method
# def _hello(): protected method
# def hello(): public method
# protected vs private  both are used to restrict access to class members out side the class but protected members can be accessed by derived classes where as private members cannot be accessed by derived classes


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
