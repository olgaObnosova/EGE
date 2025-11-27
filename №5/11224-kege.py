def f(n):
    s = ''
    while n:
        s = str(n % 3) + s
        n //= 3
    return s

sp = []
for n in range(1, 10_000):
    r = f(n)
    sm = sum([int(x) for x in str(r)])
    if sm % 4 == 0:
        r = '1' + r
        r = r[:-2]
    else:
        ost = sm % 4
        ost = ost * 3
        ost = f(ost)
        r = r + ost
    R = int(r, 3)
    if R > 353:
        sp.append(R)
sp.sort()
print(sp)