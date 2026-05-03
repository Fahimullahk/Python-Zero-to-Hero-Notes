def f(n):
    if n<=1:
        return n
    else:
        return f(n-1)+f(n-2)
n=8
for i in range(n):
    print(f(i))

