from functools import reduce
def myfunc(x, y):
    return x + y
l = [1, 2, 3, 4, 5, 7, 8]
li = reduce(myfunc, l)
print(li)

