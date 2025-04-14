def f(n):
    sp = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if i % 2 != 0:
                sp.add(i)
            if (n // i) % 2 != 0:
                sp.add(n // i)
    if len(sp) >= 5:
        return sorted(sp)
    return 0


# print(f(315))
kol = 0
for n in range(300_000_000 - 1, 1, -1):
    t = f(n)
    if t != 0 and kol < 5:
        t5 = t[-5]
        print(t5, len(t))
        kol += 1
    if kol == 5:
        break
