def f(st, end):
    if st<end or st==32:
        return 0
    elif st==end:
        return 1
    return f(st-1, end)+f(st//2, end)
print(f(51, 17)*f(17, 15)*f(15, 7))