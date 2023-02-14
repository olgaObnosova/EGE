def f(x,y):
    if x < y:
        return 0
    elif x == y:
        return 1
    else:
        return f(x-2,y) + f(x // 2,y)
print(f(28,10)*f(10,1))


