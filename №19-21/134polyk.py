def f(x,y, h):
    if (x**2+y**2)**0.5 > 20: return h%2==0
    elif h==0: return False
    c=[f(x-10,y+5, h-1), f(x-5,y-5, h-1), f(x+5,y-5, h-1)]
    return any(c) if (h-1)%2==0 else all(c)

print(19, len([x for x in range(-40, 40) if (x**2+(-1)**2)**0.5 < 20]))
print(20_1, len([x for x in range(-40, 40) if f(-1, x, 1)]))
print(20_2, len([x for x in range(-40, 40) if not f(-1, x, 1) and f(-1, x, 3)]))
print(21, [x for x in range(-40, 40) if not f(-1, x, 2) and f(-1, x,4)])