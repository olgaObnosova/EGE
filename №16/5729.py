import sys
sys.setrecursionlimit(10000)

def f(n):
    if n >= 10000:
        return n
    if n < 10000 and n % 2 == 0:
        return 1 + f(n / 2)
    if n < 10000 and n % 2 != 0:
        return n ** 2 + f(n+2)

print(f(192)-f(9))

