def hello(ab):
    def ello(*args, **kwargs):
        print("Lets start the program...")
        ab(*args, **kwargs)
        print("Thanks for comming...")
    return ello
@hello    
def add(a, b):
    print(a + b, "is the sum of these numbers")
@hello
def proud():
    print("Hello World...")

add(4, 5) 
proud()

