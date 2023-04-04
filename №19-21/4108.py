def f(a,b,m):
    if 30<=a<=45:
        return b % 2 == m % 2
    elif a>45:
        return b % 2 != m % 2
    elif b==m:
        return False
    h = [f(a+1,b+1,m),f(a*2,b+1,m)]
    #print(h)
    return any(h) if (b + 1)% 2 == m % 2 else all(h)
for a in range(1,30):
    for m in range(5):
        if f(a,0,m):
            if m==4:
                print(a,m)
            break
