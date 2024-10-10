def f(a, b, c, m):
    if a + b >= 69:
        return c % 2 == m % 2
    elif c == m:
        return False
    h = [f(a+2, b, c+1,m), f(a*2, b, c+1, m) ,\
         f(a, b+2, c+1, m) , f(a, b*2, c+1, m)]
    return any(h) if (c+1) % 2 == m % 2 else all(h)
for b in range(1, 64):

    if f(5, b, 0, 2):
        print(b)
