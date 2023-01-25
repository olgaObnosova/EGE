def f(a, b):
    if a + b > 88:
        return 0
    elif a + b == 88:
        return 1
    return f(a + b, b) + f(a, a + b)


print(f(1, 1))
