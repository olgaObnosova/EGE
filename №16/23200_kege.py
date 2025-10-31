import sys as s
s.setrecursionlimit(10_000)
def f(n):
    if n<10:
        return n
    return 3*n+f(n-3)
print((f(6250)+2*f(6244))/f(6238))
sp=[0]*6300
for i in range(6300):
    if i<10:
        sp[i]=i
    else:
        sp[i]=3*i+sp[i-3]
print((sp[6250]+2*sp[6244])/sp[6238])