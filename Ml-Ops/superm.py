class Parent:
    def __init__(self):
        print("Parent constructor")
        
    def show(self):
        print("Parent method")

class Child(Parent):
    def __init__(self):
        super().__init__()   # calling Parent constructor
        print("Child constructor")
    def show(self):
        super().show()   # call parent method
        print("Child method")

obj = Child()
obj.show()