def f(a, h, ph):
    if a >=301:
        return h%2==ph%2
    elif h==ph:
        return 0
    comb=[f(a+3, h+1, ph), f(a*5, h+1, ph)]
    return any(comb) if (h+1)%2==ph%2 else all(comb)
for a in range(1, 301):
    for ph in range(5):
        if f(a,0,ph):
            if ph==3:
                print(a)
            break