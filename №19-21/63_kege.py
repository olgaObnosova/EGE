def f(a, b, c, m):
    if a + b >= 80:
        return c % 2 == m % 2
    if c == m:
        return False
    h = [f(a + 1, b, c + 1, m), f(a, b + 1, c + 1, m)]
    return any(h) if (c + 1) % 2 == m % 2 else all(h)


for b in range(1, 80):
    for m in range(5):
        # если Ваня 1м ходом, то m=2
        # если Петя 2м ходом, то m=3
        # если Ваня 2м ходом, то m=4
        if f(20, b, 0, m):
            if m == 3:
                print(b, m)
            break
