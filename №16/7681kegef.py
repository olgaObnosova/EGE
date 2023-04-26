from functools import lru_cache
@lru_cache
def f(n):
    if n<=4:
        return 1
    return f(n-1)+f(n-3)+g(n-2)
def g(n):
    if n>1500:
        return 5
    return g(n+1)+g(n+2)+1
print((f(1200)+g(100))%10000)