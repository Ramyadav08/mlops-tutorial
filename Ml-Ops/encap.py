class Employee:
    def __init__(self):
        self.__salary = 50000   # private variable

    def get_salary(self):
        return self.__salary

    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount
        else:
            print("Invalid salary")

emp = Employee()

print(emp.get_salary())   # 50000

emp.set_salary(100)      # Invalid salary(-100)
print(emp.get_salary())