from functools import *
@lru_cache(None)


def f(n):
    if n <= 1:
        return 1
    elif n > 1 and n % 3 == 0:
        return 2 * f(n - 1) + f(n - 2)
    else:
        return 3 * f(n - 2) + f(n - 1)

def sm(a):
    s = 0
    while a > 0:
        s += a % 10
        a //= 10
    return s

k = 0
for i in range(1, 35):
    if sm(f(i)) % sm(f(i)) == 0 and sm(f(i)) % 1 == 0 and sm(f(i)) % 2 != 0 and sm(f(i)) % 3 != 0  and sm(f(i)) % 5 != 0  and sm(f(i)) % 7 != 0:
        k += 1
print(k)