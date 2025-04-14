def f(n):
    sp = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sp.add(i)
            sp.add(n // i)
    if len(sp) >= 5:
        return sorted(sp)
    return 0


# print(f(1369863))
kol = 0
for n in range(100_000_000-1, 1, -1):
    t = f(n)
    t5 = 0
    if t != 0 and kol < 5:
        t5 = t[-5]
        print(t5, len(t))
        kol += 1
    if kol == 5:
        break
