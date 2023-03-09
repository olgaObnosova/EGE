def f(a,h,ph):
    if a>20:
        return h%2==ph%2
    elif h==ph:
        return 0
    hod=[f(a+1,h+1,ph),f(a*2,h+1,ph)]
    return any(hod) if (h+1)%2==ph%2 else all(hod)
for a in range(1,20):
    for ph in range(5):
        if f(a,0,ph):
            if ph==4:
                print(a)