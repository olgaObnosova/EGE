def f(st, end, k):
    if st > end or st==23 or '11' in k:
        return 0
    elif st==end and '11' not in k:
        return 1
    return f(st+1, end, k+'1')+f(st+2, end, k+'2')\
        +f(st*2, end, k+'3')
print(f(3, 11, '')*f(11, 79, ''))