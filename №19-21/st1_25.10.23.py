def f(s,h,ph):
    if s>=108:
        return h%2==ph%2
    elif h==ph:
        return False
    comb = [f(s*(1.5+0.5*(s%2)), h+1,ph), f(s+1, h+1, ph)]
    return any(comb) if (h+1)%2==ph%2 else  all(comb)
for s in range(1, 108):
    for ph in range(5):
        if f(s, 0, ph):
            if ph==4:
                print(s)
            break
