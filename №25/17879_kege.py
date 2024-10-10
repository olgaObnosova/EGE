def delit(n):
    sp=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            sp.add(i)
            sp.add(n//i)
    return list(sp)
k=0
for i in range(800_001, 10**10):
    t = delit(i)
    if len(t)!=0:
        m = min(t) + max(t)
    else:
        m=0
    if m % 10 == 4:
        print(i, m)
        k+=1
        if k==5:
            break
