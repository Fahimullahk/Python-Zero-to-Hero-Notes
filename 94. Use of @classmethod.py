class employee:
    company = "Apple"
    def show(self):
        print(f"The employee name is {self.name} and a hardworking in {self.company} company")
    
    @classmethod
    def anothercomp(cls, anocomp):
        cls.company = anocomp
    
emp1 = employee()
emp1.name = "Fahim"
emp1.show()
emp1.anothercomp("Amazon")
emp1.show()
print(employee.company)


"""Here, in the above example we created a simple class and 
defined a show() method. Here in the class we create a 
variable company=Apple, so when we access this class with 
anothermehod() method we can change the company with given 
changed company name. But here the class variable company name 
will remains Apple will never effect any change in the class variable. 
However, if we use the @classmethod decorator we can change the 
class variable as we can see in the above example the class variable 
has been changed."""
