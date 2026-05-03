class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
p = Person("John", 30)
p.__dict__


# """The __dict__ attribute returns a dictionary representation of an objects attributes. 
# It is a useful tool for introspection. """