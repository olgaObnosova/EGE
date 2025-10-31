def fn(x, y, a):
    return (x-3*y<a) or (y>400) or (x>56)
def f(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not fn(x, y, a):
                return False
    return True
for a in range(100):
    if f(a):
        print(a)


