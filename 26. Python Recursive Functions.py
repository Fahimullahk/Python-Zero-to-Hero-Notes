def factorial(n):
    if (n == 0) or (n==1):
        return 1
    else:
        return (n * factorial(n-1))
n = int(input("Enter the number for finding factorial"))
print("Number : ", n)
print("Factorial of Number is :", factorial(n))

