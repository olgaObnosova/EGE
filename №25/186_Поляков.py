def f(n):
    s = set()
    c = 1
    m = 0
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            s.add(i)
            s.add(n//i)
    if len(s) >= 5:
        for x in list(s):
            c *= x
        return c
    else:
        return 0
c = 0
for r in range(500000000, 10 ** 10):
    t = f(r)
    if int(t) % 100 == 91 and int(t) < r:
        print(r)
        c += 1
    if c == 5:
        break