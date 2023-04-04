def f(s, e):
    if s > e or s == 20:
        return 0
    elif s == e:
        return 1
    return f(s + 1, e) + f(s * 2, e)


print(f(1, 10) * f(10, 40))
