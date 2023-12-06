def f(st, end):
    if st> end or st==12:
        return 0
    elif st==end:
        return 1
    return f(st+1,end)+f(st*2, end)+f(st**2, end)
print(f(3, 25))
