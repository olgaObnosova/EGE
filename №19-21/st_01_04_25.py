def f(a, b, h):
    if (a+b)<=150:
        return h%2==0
    elif h==0:
        return False
    comb=[f(a-2, b, h-1), f(a, b-2, h-1), \
          f(a//3, b, h-1), f(a, b//3, h-1)]
    return any(comb) if (h-1)%2==0 else all(comb)
print([x for x in range(135, 500) if f(x, 17, 2)])
print([x for x in range(135, 500) if f(x, 17, 3) and not f(x, 17, 1)])
print([x for x in range(135, 500) if f(x, 17, 4) and not f(x, 17, 2)])