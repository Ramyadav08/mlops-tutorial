class Employee:
    def __init__(self):
        self.__salary = 50000

    def get_salary(self):
        return self.__salary

emp = Employee()
print(emp.get_salary())   # calling method


class Employee1:
    def __init__(self):
        self.__salary = 50000

    @property
    def salary(self):
        return self.__salary

emp1 = Employee1()
print(emp1.salary)   # looks like variable


"""@property allows you to:

Access a method like a variable
while still keeping control & validation logic inside.
"""