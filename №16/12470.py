from functools import lru_cache

@lru_cache(None)
# import sys
# sys.setrecursionlimit(2000)
def f(n):
    if n < 3:
        return n
    elif n > 2 and n % 2 != 0:
        return f(n - 1) + f(n - 2) + 1
    return sum([f(x) for x in range(1, n)])


print(f(38))
sp=[0]*39
sp[1]=1
sp[2]=2
for i in range(3,39):
    if i%2!=0:
        sp[i]=sp[i-1]+sp[i-2]+1
    else:
        sp[i]=sum(sp[:i])
print(sp[38])