def f(st, e):
    if st>e or st==35:
        return 0
    elif st==e:
        return 1
    return f(st+2, e)+f(st+5, e)+f(st*3, e)
print(f(5,20)*f(20,40))