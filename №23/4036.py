def f(x, y):
    if y == 15:
        
    if x == y:
        return 1
    else:
        return f(x * 2, y) + f(x * 2 + 1, y)
print(f(2, 10) * f(10, 15))