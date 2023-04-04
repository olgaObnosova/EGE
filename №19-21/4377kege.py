def f(a,b,m):
    if a>=26:
        return b % 2 == m % 2
    elif b==m:
        return False
    h = [f(a+1,b+1,m),f(a+2,b+1,m), f(a+(a%2)*a,b+(a%2),m)]
    #print(h)
    return any(h) if (b + 1)% 2 == m % 2 else all(h)
for a in range(1,26):
    for m in range(6):
        if f(a,0,m):
            if m==3:
                print(a,m)
            break