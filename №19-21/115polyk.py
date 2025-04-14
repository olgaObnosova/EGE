def f(a, h):
    if a%10==0: return h%2==0
    elif h==0: return False
    comb=[f(a+1, h-1), f(a+3, h-1),f(a+11, h-1)]
    return any(comb) if (h-1)%2==0 else all(comb)

print(19, [x for x in range(11, 100) if f(x, 2)])
print(20, len([x for x in range(11, 100) if not f(x, 1) and f(x, 3)]))
print(21, sum([x for x in range(11, 100) if not f(x, 2) and f(x, 4)]))