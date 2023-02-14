import math as m
def f(x, y):
    if x == y:
        return 1
    if x > y:
        return 0
    else:
        return f(x + 1, y) + f(x + 4, y) + f(m.factorial(x), y)
print(f(2, 24))