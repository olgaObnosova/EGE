#https://kompege.ru/variant?kim=25003645
from functools import lru_cache

@lru_cache
def f(n):
    if n==0:
        return 0
    elif n<3:
        return 1
    else:
        return f(n-1)+f(n-2)
print(f(47))
