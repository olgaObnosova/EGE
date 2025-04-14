def f(x, y, z, w):
    return (x == (y <= z)) and(y == (not(z <= w)))
import itertools as t
for a1, a2, a3, a4 in t.product([0, 1], repeat = 4):
    table = [(0, 0, a1, 0), (a2, 0, a3, 0), (1, 0, 1, a4)]
    if len(table) == len(set(table)):
        for p in t.permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 0]:
                print(*p, sep='')
