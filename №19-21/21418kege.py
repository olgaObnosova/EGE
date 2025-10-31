def f(a, h):
    if a<=87:
        return h%2==0
    elif h==0:
        return False
    comb=[f(a-2, h-1), f(a//2, h-1)]
    return any(comb) if (h-1)%2==0 else all(comb)
print([x for x in range(89, 250) if f(x, 2)]) #19
print([x for x in range(89, 250) if f(x, 3) and not f(x, 1)]) #20
print([x for x in range(89, 250) if f(x, 4) and not f(x, 2)]) #21