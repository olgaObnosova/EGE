def f(st, e):
    if st>e or st==38:
        return 0
    elif st==e:
        return 1
    return f(st+3, e)+f(st+5, e)+f(st*4, e)
print(f(8,30)*f(30,50))