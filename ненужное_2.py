import sys as s
s.setrecursionlimit(100_000)
import time as t
def f(n):
    if n==1:
        return 1
    return n*f(n-1)
start = t.time()
print((f(2024)//4+f(2023))//f(2022))
end= t.time()
print(end - start)
print(t.process_time())

