def average(*numbers):
    num = 0
    for i in numbers:
        num=num+i
    print("The average of numbers is:", num/len(numbers))
average(16, 17, 18)

