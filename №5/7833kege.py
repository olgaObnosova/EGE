def f(n):
    s = ''
    while n > 0:
        s += str(n % 3)
        n = n // 3
    return s[::-1]


minn = float('inf')
for i in range(10, 1000):
    n = f(i)
    if i % 2 == 0:
        n = n + n[-2:]
    else:
        sm = 0
        for x in n:
            sm += int(x)
        n = n + f(sm)
    r = int(n, 3)
    #print(r, i)
    if r < minn:
        minn = r
        otv = i
print(otv)
