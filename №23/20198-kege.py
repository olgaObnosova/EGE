def f(st, end, s):
    if 'AAA' in s or st >37:
        return 0
    elif st==end and 'AAA' not in s:
        return 1
    return f(st-1, end, s + 'A')+\
        f(st+5, end, s + 'B') + \
        f(st *2, end, s + 'C')
print(f(5, 34, ''))