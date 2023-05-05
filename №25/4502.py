def f(n):
    d = 2
    while d * d <=n and n% d != 0:
        d += 1
    return d * d > n
a=[]
for i in range(3000000,10000000+1):
    if f(i) == True:
        a.append(i)
count = 0
c = []
for g in range(len(a)-1):
    if a[g +1] -a[g] == 2:
        count += 1
        c.append(a[g+1]+a[g])
print(count, int(c[-1]/2))