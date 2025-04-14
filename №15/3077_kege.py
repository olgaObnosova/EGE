def fn(x, y, a):
    return (680*y+256*x<a) or (5*x+3*y>11111)
def f(a):
    for x in range(1, 1_000_000):
        for y in range(1, 1_000_000):
            if not fn(x, y, a):
                return False
    return True
for a in range(3_000_000):
    if f(a):
        print(a)