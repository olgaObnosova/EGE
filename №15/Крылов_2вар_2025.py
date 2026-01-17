def dl(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s
a = range(7, 27)
b = dl(77)
for y in range(1, 1000):
    c = dl(y)
    f=1
    if len(c)>0:
        for x in range(1000):
            f*=(x in c)<=((x in a) and (x not in b))
        if f:
            print(y)
