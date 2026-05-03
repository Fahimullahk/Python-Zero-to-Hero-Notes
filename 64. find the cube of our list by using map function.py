def myfunc(x):
    return x*x*x
l = [1, 2, 3, 4, 5, 7, 8]
li = list(map(myfunc, l))
print(li)

