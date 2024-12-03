for a in range(300):
    f=1
    for x in range(90, 101):
        f*=(x&79!=0) and ((x&31!=0) or (x&a!=0))
    if f:
        print(a)


