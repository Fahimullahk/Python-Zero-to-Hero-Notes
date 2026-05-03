x = int(input("Write your number.."))
match x:
     case _ if x == 0:
        print("x value is equal to :", x)
     case _ if x > 50:
        print("x value is smaller than :", x+1)
     case _ if x == 49:
        print("x value is equal to :", x)
     case _:
        print(x)

