def f(s, h, max_h):
    if s > 128:
        return h % 2 == max_h % 2
    if h == max_h:
        return 0
    if h % 2 != max_h:
        return f(s + 1, h + 1, max_h) or f(s * 2, h + 1, max_h)
    else:
        return f(s + 1, h + 1, max_h) and f(s * 2, h + 1, max_h)
for x in range(1, 129):
    for j in range(1,10):
        if f(x, 0, j):
            print(x,j)
            break
