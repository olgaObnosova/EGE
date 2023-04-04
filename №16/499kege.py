def f(n):
    if n < 50:
        return n
    if n > 49:
        return 2 * g(50 - n // 2)


def g(n):
    if n > 40:
        return 10
    if n < 41:
        return 30 + f(n + 600 // n)


print(f(80))
