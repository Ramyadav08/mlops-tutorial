# when one class acquires the properties of another class, it is known as inheritance.

class car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.brand} {self.model}"
    

class ToyataCar(car):
    def __init__(self, brand, model, year, fuel_type):
        super().__init__(brand, model, year) # super is used to access method of parent class
        self.fuel_type = fuel_type

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Fuel Type: {self.fuel_type}"
    
toyota = ToyataCar("Toyota", "Camry", 2020, "Gasoline")
print(toyota.display_info())


#class method is bound to the class and receives the class as the first argument
#static method can not access or modify class state
class Person:
    name="ram"

    def changename(self,name):
        # self.name=name 
        # Person.name=name  # modifying class attribute using class name
        self.__class__.name=name  # modifying class attribute using __class__

    @classmethod
    def changeclsname(cls,name):
        cls.name=name
p=Person()
p.changename("shyam")
print(p.name)
print(Person.name) # class attribute remains unchanged

# property decorator is used to define getter method for a class attribute
