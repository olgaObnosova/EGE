def f(a,b, h):
    if a>=78 or b>=78:
        return h%2==0
    elif h==0:
        return False
    comb=[]
    if a==b:
        comb.append(f(a + 1, b, h - 1))
        comb.append(f(a + 2, b, h - 1))
        comb.append(f(a + 3, b, h - 1))
        comb.append(f(a, b + 1, h - 1))
        comb.append(f(a, b + 2, h - 1))
        comb.append(f(a, b + 3, h - 1))
    elif a>b:
        comb.append(f(a + 1, b, h - 1))
        comb.append(f(a + 2, b, h - 1))
        comb.append(f(a + 3, b, h - 1))
        comb.append(f(a, b *2, h - 1))
    else:
        comb.append(f(a, b + 1, h - 1))
        comb.append(f(a, b + 2, h - 1))
        comb.append(f(a, b + 3, h - 1))
        comb.append(f(a * 2, b, h - 1))
    return any(comb) if (h-1)%2==0 else all(comb)
s=[]
for x in range(1, 78):
    for y in range(1, 78):
        if f(x, y, 1):
            s.append(x+y)

print(min(s))
print(20, [x for x in range(1,78) if not f(25, x, 1) and f(25, x, 3)])
print(21, [x for x in range(1,78) if not f(69, x, 2) and f(69, x, 4)])
