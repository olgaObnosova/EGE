def f(st, end):
    if st<end or st==7:
        return 0
    elif st==end:
        return 1
    return f(st-1, end) + f(st-4, end) + f(st//3, end)
print(f(19, 13) * f(13, 2))