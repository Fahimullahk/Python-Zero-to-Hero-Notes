class banda():
    def __init__(self, a, b, c):
        self.name = a
        self.age = b
        self.occupation = c
    def insan(self):
        print("The employee name is",self.name, "he is ", self.age, "years old. And he is working as a", self.occupation,".")
ab = banda("Fahim Ullah", 37, "Developer")
bb = banda("Zeeshan", 38, "developer")
cb = banda("Abdul Salam", 38, "HR")
ab.insan()
bb.insan()
cb.insan()

