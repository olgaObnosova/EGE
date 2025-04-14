def f(a,b,  h):
    if a + b>=62:
        return h%2==0
    elif h==0:
        return False
    comb=[f(a+b, b, h-1), f(a, a+b, h-1)]
    return any(comb) if (h-1)%2==0 else all(comb)
print(19, [x for x in range(1, 52) if f(10,x,1)])
print(20, [x for x in range(1, 52) if not f(10,x,1) and f(10, x, 3)])
print(21, [x for x in range(1, 52) if not f(10,x,2) and f(10, x, 4)])