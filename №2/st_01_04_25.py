import itertools as t
def f(x, y, z, w):
    return ((x and y) or ((1-x))) and w or z
for a1, a2, a3, a4, a5, a6 in t.product([0,1], repeat = 6):
    table = [(0, a1, 0, a2),(a3, 1, a4, 1),(a5, 1, 1, a6)]
    if len(table)==len(set(table)):
        for p in t.permutations('xyzw', r=4):
            if [f(**dict(zip(p, r))) for r in table]==[1, 0, 0]:
                print(*p)