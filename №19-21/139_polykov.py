def f(a,b, h):
    if a+b>=227: return h%2==0
    elif h==0: return False
    c=[f(a+1,b, h-1), f(a*2,b, h-1), f(a,b+1, h-1), f(a,b*2, h-1)]
    return any(c) if (h-1)%2==0 else all(c)


print(19, [x for x in range(1, 210) if f(17, x, 2)])
print(20, [x for x in range(1, 210) if not f(17, x, 1) and f(17, x, 3)])
print(21, [x for x in range(1, 210) if not f(17, x, 2) and f(17, x, 4)])