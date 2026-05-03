def fun(fx, x):
    return 6 + fx(x)
y = lambda x: x*x*x
print(fun(y, 3))

