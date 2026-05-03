class Manager:
    def __init__(self, name, age, id):
        self.name = name
        self.age = age
        self.id = id

class Employee(Manager):
    def __init__(self, name, age, id, lang):
        super().__init__(name, age, id)
        self.lang = lang

a = Manager("Abdul Salam", "38", "1")
print(a.name)
print(a.age)
print(a.id)
print("------------------")
b = Employee("Fahim Ullah", "37", "5", "Python")
print(b.name)
print(b.age)
print(b.id)
print(b.lang)


