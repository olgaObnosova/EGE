import sys

sys.setrecursionlimit(30000)


def f(x, y, z):
    if x > y:
        return 0
    if x == y:
        return 1
    if x < y and z == 1:
        return f(x * 2, y, 2) + f(x + 3, y, 3)
    if x < y and z == 2:
        return f(x + 1, y, 1) + f(x + 3, y, 3)
    if x < y and z == 3:
        return f(x + 1, y, 1) + f(x * 2, y, 2)

    return f(x + 1, y, 1) + f(x * 2, y, 2) + f(x + 3, y, 3)


print(f(20789, 45789, 0))