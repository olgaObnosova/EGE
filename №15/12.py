
for a in range(1, 1000):
    f = 1
    for x in range(1, 1000):
        f *= (x&a==0 or x&36!=0 or x&6!=0)
    if f:
        print(a)
