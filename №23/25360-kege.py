def f(st, end):
    if st==end:
        return 1
    elif st<end or st==36:
        return 0
    return f(st-3, end)+f(st-6, end)+f(st//2, end)
print(f(86, 53)*f(53, 12))