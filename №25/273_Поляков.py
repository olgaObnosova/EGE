import math
def f(n):
    sp = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            sp.add(i)
            sp.add(n//i)
    if len(sp) >= 6:
        sp = sorted(list(sp)[0:6])
        a1 = sp[0]
        a2 = sp[1]
        a3 = sp[2]
        a4 = sp[3]
        a5 = sp[4]
        a6 = sp[5]
        if math.gcd(a1, a2, a3, a4, a5, a6) == 1:
            return list(sp)
cnt = 0
for n in range(1_000_000_000, 900_000_000, -1):
    a = f(n)
    if a != None:
        cnt += 1
        print(n, max(a))
        if cnt == 5:
            break