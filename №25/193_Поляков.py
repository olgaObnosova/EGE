def f(n):
    l = set()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            l.add(i)
            l.add(n//i)
    if len(l) >= 7:
        return 1, sorted(list(l), reverse=True)
    else:
        return 0, list(l)
k = 0
for i in range(400_000_000, 1_000_000_000):
    s = f(i)
    if s[0]:
        k += 1
        print(i, s[1][6], len(s[1]))
        if k == 5:
            break