def f(st, end):
    if st>end or st==35:
        return 0
    elif st==end:
        return 1
    return f(st+1, end)+f(st+2, end)+f(st*2, end)
print(f(7, 13)*f(13,15)*f(15, 51))
