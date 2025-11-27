def f(x, m):
    if x == 98 or x == 99: return m % 2 == 1
    if m == 0: return 0
    if x < 50:
        g = [f(x+2, m-1), f(x+4, m-1), f(x*2, m-1)]
    if x >= 50:
        g = [f(x+2, m-1), f(x+4, m-1)]
    if x >= 96:
        g = [f(x+2, m-1)]
    return any(g) if m % 2 == 0 else all(g)
print([x for x in range(1, 100) if (not f(x, 3)) and f(x, 5)])
a = [x for x in range(1, 100) if (not f(x, 2)) and f(x, 4)]
print(a[0], a[-1])