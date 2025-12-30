class sum:
    name="ramrekha" # class attribute
    def __init__(self,a,b, name):  # constructor
        self.A=a
        self.B=b
        self.name=name  # obj attr > class attr
    def add(self):    # method are the function that belongs to object
        return self.A+self.B
s=sum(10,20,"ramrekhayadav") 
print(s.add())
print(s.name)  # it will print obj attr


class Students:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    
    @staticmethod
    def hello():
        print("Hello Students")

    def average(self):
        sum=0
        for val in self.marks:
            sum+=val
        return sum/len(self.marks)
    
s1=Students("ram",[100,90,80])
s1.hello()  
print(s1.name)
print(s1.average())
print("********************************")

# static method that don't use the self parameter (work at class level)



