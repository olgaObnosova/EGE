def f(n):
    a=0
    a1=0
    s = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            d1 = sum(map(int, str(i)))
            if d1 == 17:
                s.add(i)
            d2 = sum(map(int, str(n//i)))
            if d2 == 17:
                s.add(n//i)
    if len(s) >=5:
        return sorted(s)
    return 0


k=0
for n in range(300_000_000 - 1, 1, -1):
    t=f(n)
    if t != 0 and k < 5:
        t5 = t[-5]
        print(t5, len(t))
        k += 1
    if k==5:
        break