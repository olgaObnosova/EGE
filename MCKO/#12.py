def f(a, b, h):
    if (a+b)<=64:
        return h%2==0
    elif h==0:
        return False
    com = [f(a-2, b, h-1), f(a, b-2, h-1),\
           f(a-6, b, h-1), f(a, b-6, h-1),\
           f(a//3, b, h-1), f(a, b//3, h-1)]
    return any(com) if (h-1)%2==0 else all(com)
print([x for x in range(7, 65) if f(x, 58, 2)])
print([x for x in range(7, 65) if f(x, 58, 3) and not f(x, 58, 1)])
print([x for x in range(7, 65) if f(x, 58, 4) and not f(x, 58, 2)])