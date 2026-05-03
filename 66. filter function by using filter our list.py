def myfunc(x):
    return x > 2
l = [1, 2, 3, 4, 5, 7, 8]
li = list(filter(myfunc, l))
print(li)

