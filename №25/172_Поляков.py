    d=set()
    v=0
    a=0
    for i in range(2, int(n**5)+1):
        if n%i==0:
            if i!=1 and i!=n:
                d.add(i)
                d.add(n // i)
    if len(d)>0:
        for s in list(d):
            a+=s
            v+=1
    r=int(a/v)
    if r==0 or len(d)==0:
        return 0
    else:
        return r

print(f(6697))
z=0
for x in range(550000, 10**10):
    t=f(x)
    if t!=0:
        if t%31==13:
            print(x, t)
            z += 1
            if z == 5:
                break