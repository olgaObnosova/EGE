import sys as s
s.setrecursionlimit(1_000_000)
def f(n):
    if n<=10:
        return n
    return n-7+f(n-21)
print((f(185_734)-f(185_650))/f(40))