def fact(n):
    d = 2
    sp = set()
    while n % 2 == 0:
        sp.add(2)
        n = n // d
    d = 3
    while d * d <= n:
        if n % d == 0:
            sp.add(d)
            n = n // d
        else:
            d += 1
    if n > 0 and n != 1:
        sp.add(n)
    return len(sp)


a, b = map(int, input().split())
for i in range(a, b + 1):
    print(fact(i), end=' ')
