def f(x, y, z, w):
    return (w==(z!=y)) and (z==(y<=x))
import itertools as t
for a1, a2, a3, a4, a5, a6, a7 in t.product([0, 1], repeat =7):
    table=[(a1, 0, 0, a2), (a3,0,a4,0), (a5,a6,a7,0)]
    if len(table)==len(set(table)):
        for p in t.permutations('xyzw'):
            if [f(**dict(zip(p, r))) for r in table] == [1, 1, 1]:
                print(*p, sep='')