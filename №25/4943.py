def f(N):
    s = set()
    for d in range(2, int(N**0.5)+1):
        if N % d == 0:  # делитель
            if d % 2 != 0:  # нечетный делитель
                s.add(d)
            dd = N // d  # обратный делитель
            if dd % 2 != 0:  # нечетный обратный делитель
                s.add(dd)
    if len(s) >= 5:
        return (sorted(s)[-5], len(s))
    else:
        return (0, 0)


cnt = 0  # счетчик результатов
res = []
for N in range(300_000_000-1, 0, -1):
    D, n = f(N)
    if D > 0:
        res.append((D, n))
        cnt += 1
        if cnt == 5:
            break

for D, n in reversed(res):
    print(D, n)
