def f(st, end, k):
    if k>15:
        return '0'
    elif k==15:
        return st
    return f(st+sum([int(x) for x in st]), end, k+1) \
        + f(st[-1:]+st[:-1], end, k+1)
s=set()
for i in range(15, 10_000):
    t=f(str(15),str(i),0)
    if t:
        s.add(t)
print(s)