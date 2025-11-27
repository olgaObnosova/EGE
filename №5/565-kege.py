sch = 0
for n in range(100, 201):
    n = str(n)
    n = sorted(n)
    if n[0]!='0':
        k1 = int(n[-1] + n[1])
        k2 = int(n[0] + n[1])
    elif n[1]!='0':
        k1 = int(n[-1] + n[1])
        k2 = int(n[1] + n[0])
    else:
        k1 = int(n[-1] + n[1])
        k2 = int(n[-1] + n[0])
    print(k1, k2, n)
    if k1 - k2 == 30:
        sch += 1
print(sch)