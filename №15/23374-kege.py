def fn(x, y, a):
    return (x<a) and (y< 3*a) or (2*x+y>128)
def pr(a):
    for x in range(1, 1000):
        for y in range(1, 1000):
            if not(fn(x, y, a)):
                return False
    return True
for a in range(1, 1000):
    if pr(a):
        print(a)