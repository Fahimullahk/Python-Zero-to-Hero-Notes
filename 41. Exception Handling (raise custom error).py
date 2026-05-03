a = input("Enter your obtained Marks percentage or write quit to leave...")
if a.lower() == "quit":
    print("Good bye....")
else:
    try:
        a = int(a)
        if a > 70 and a < 100:
            print("You are eligible for the job")
        else:
            print("You are not eligible for job")
    except:
        print("Invalid Entry: enter your total obtained marks between 70 and 100")

