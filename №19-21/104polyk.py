def f(a, h):
    if a>=166:
        return h%2==0
    elif h==0:
        return False
    comb=[f(a + 10, h-1), f(a + 2, h-1)]
    for i in range(2, 100):
        if a*i-a>80:continue
        else:
            comb.append(f(a*i, h-1))
    return any(comb) if (h-1)%2==0 else all(comb)
print(19, [x for x in range(1, 166) if f(x, 1)])#1
print(20, [x for x in range(1, 166) if (not f(x, 1)) and f(x, 3)])
print(21, [x for x in range(1, 166) if not f(x, 2) and f(x, 4)])

