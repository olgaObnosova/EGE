def ppr(z1, z2):
    if z1<z2:
        z = z1
    else:
        z = z2
    for w in range(2, int(z**0.5) + 1):
        if z1 % w == 0 and z2 % w == 0:
            return False
    if z1 % z2 == 0 or z2 % z1 == 0:
        return False
    return True
def f(n):
    s = []
    for i in range(2, int(n**0.5)+1):
        if n % i == 0 and i != (n // i):
            s.append(i)
            s.append(n // i)
        elif n % i == 0 and i == (n // i):
            s.append(i)
    s = sorted(s)
    if len(s) > 2 and ppr(s[0], s[1]) and ppr(s[1], s[2]) and ppr(s[0], s[2]):
        return max(s)
    else:
        return 0
k = 0
for x in range(100000000,150000000):
    d = f(x)
    if k == 7:
        break
    if d > 0:
        print(x, d)
        k = k + 1