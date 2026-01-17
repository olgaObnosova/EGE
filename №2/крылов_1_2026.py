def f(x, y, z, w):
    return x <= (not ((y <= z) and (z != w)))
import itertools as t
for a1, a2, a3, a4,a5 in t.product([0,1], repeat =5):
    table = [(0, a1,a2,0),(a3, 1, 1, a4),(a5, 1, 0, 0)]
    if len(table)==len(set(table)):
        for p in t.permutations('xyzw', r=4):
            if [f(**dict(zip(p,r))) for r in table]==[0,0,0]:
                print(*p)