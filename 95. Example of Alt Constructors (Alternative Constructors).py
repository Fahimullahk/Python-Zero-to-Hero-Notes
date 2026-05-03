class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def fstri(cls, stri):
        return cls(stri.split("-")[0], int(stri.split("-")[1]))

emp1 = employee("Fahim Ullah", 36)
print(emp1.name)
print(emp1.age)

stri = ("Haris Jan-30")
emp2 = employee.fstri(stri)
print(emp2.name)
print(emp2.age)

