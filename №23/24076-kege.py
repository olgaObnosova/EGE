def f(st, end):
    if st < end or st==22: # избегать
        return 0
    elif st==end:
        return 1
    return f(st-2, end)+f(st-5, end) + f(st//2, end)
print(f(47, 30) * f(30, 11)) # посетить 30

