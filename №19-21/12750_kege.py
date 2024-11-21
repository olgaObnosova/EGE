def f(s,h,ph):
    if s>=121:
        return h%2==ph%2
    elif h==ph:
        return False
    comb = [f(s+1, h+1,ph), f(s+2, h+1, ph), f(s+3, h+1, ph),\
            f(s+4, h+1, ph), f(s*2, h+1, ph)]
    return any(comb) if (h+1)%2==ph%2 else  all(comb)
for s in range(1, 60):
        if f(s, 0, 4) and not f(s, 0, 2):
           print(s)
