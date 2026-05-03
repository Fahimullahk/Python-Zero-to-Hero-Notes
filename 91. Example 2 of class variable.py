class Student:
    Institute = "CSUniversity"  # This is a class variable.
    def __init__(self, name):
        self.name = name
        self.level = 14

    def show(self):
        print(f"The name of student is {self.name} and studying in class {self.level} of {self.Institute}")

s1 = Student("Haris")
s1.show() 
s2 = Student("Rizwan")
s2.level = 16
s2.show()

