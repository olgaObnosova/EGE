def f(n):
    d=set()
    v=0
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            if i!=1 and i!=n:
                d.add(i)
                d.add(n//i)
    if len(d)>=3:
        for s in list(d):
            v+=s
        return v
    else:
        return 0

v=0
for x in range(10000000, 10**10):
    t=str(f(x))
    if t.count('7')>=4:
        print(x, t)
        v+=1
        if v==5:
            break