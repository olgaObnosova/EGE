def f(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if pr(i):
                s.add(i)
            if pr(n//i):
                s.add(n//i)
    return s
def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
r=set()
for i in range(485_617, 529_679):
    t = f(i)
    cif=[]
    if len(t)>2 and max(t)-min(t)<100:
        for z in t:
            for y in t:
                for w in t:
                    if z!= w and z!= y and w!=y \
                            and z%10==y%10 and y%10==w%10 and z%10==w%10 and\
                        z*w*y==i:
                        r.add((i, max(t)-min(t)))
print(r)


