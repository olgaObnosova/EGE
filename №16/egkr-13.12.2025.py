import sys as s
s.setrecursionlimit(10**6)
def f(n):
    if n>=21:
        return f(n-5)+3480
    return 10*(g(n-9)-30)
def g(n):
    if n>=264_685:
        return n/20 +33
    return g(n+9)-2
print(f(675))