def func():
    try:
        a = int(input("Enter the Number for finding its table :"))
        for i in range(1, 11):
            print(a, "x", i, "=", a*i)
            return 
    except:
        print("You entered an invalid number")
    print("All weather thundering, i will be executed..")
func()

