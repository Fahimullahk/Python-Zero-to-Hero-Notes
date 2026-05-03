def fabonacci(n):
    if n<=1:
        return n
    else:
        return fabonacci(n-1) + fabonacci(n-2)
n = int(input("Enter the number for finding fabonacci"))
print("Number : ", n)
print("fabonacci of Number is :", fabonacci(n))

