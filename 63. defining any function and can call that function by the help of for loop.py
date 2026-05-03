def myfunc(x):
    return x*x*x
l = [1, 2, 3, 4, 5, 7, 8]
li = []
for i in l:
    li.append(myfunc(i))
print(li)

