def s(n):
    e = set()
    sp = []
    count = 0
    x1 = 0
    x2 = 0
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            e.add(i)
            e.add(n//i)
    sp = list(e)
    sp.sort()
    if len(sp) < 2:
        return 0
    else:
        x1 = sp[-1]
        x2 = sp[-2]
        count = x1+x2
        return count

count1 = 0
for g in range(10000000, 10**10):
    t = s(g)
    if t < 100000 and t%31 == 0 and t!=0:
        count1 += 1
        print(g, t)
    elif count1 == 5:
        break