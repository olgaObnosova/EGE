import sys as s
s.setrecursionlimit(10**6)
def f(n):
    if n>=19:
        return f(n-4)+3580
    return 6*(g(n-7)-36)
def g(n):
    if n>=248_045:
        return n/20 +28
    return g(n+9)-4
print(f(673))