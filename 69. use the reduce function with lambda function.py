from functools import reduce
l = [1, 2, 3, 4, 5, 7, 8]
li = reduce(lambda x, y: x + y, l)
print(li)

