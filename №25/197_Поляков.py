def f(n):
    sp=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if i%2==0:
                sp.add(i)
            if (n//i)% 2 == 0:
                sp.add(n//i)
    if len(sp)>=6:
        return sorted(sp)
    return 0
kol=0
for n in range(300_000_00-1, 1, -1):
    g=f(n)
    if g!=0 and kol<6:
        g5= g[-5]
        print(g5, len(g))
        kol+=1
    if kol == 5:
        break