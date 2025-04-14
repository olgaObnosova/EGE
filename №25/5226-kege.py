import fnmatch as t
def f(n):
    s=set()
    for i in range(1, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return list(s)
sp=[]
for i in range(31_622, 37_000):
    sp.append(i**2)
print(sp)
for x in sp:
    if t.fnmatch(str(x), '1*2*7*04'):
        r = f(x)
        r.sort()
        if len(r)==45:
            print(x, r[-2])
