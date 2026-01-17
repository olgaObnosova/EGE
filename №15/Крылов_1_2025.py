def dl(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s
a = range(3, 61)
b = dl(177)
print(b)
for y in range(1, 5000):
    f=1
    c=dl(y)
    if len(c)>0:
        for x in range(1, 5000):
            f*=((x in c)<=((x in a) and (x not in b)))
        if f:
            print(y)
