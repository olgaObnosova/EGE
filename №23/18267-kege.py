def f(st, end, s):
    if st==end and s[-1]!='C':
        return 1
    elif st>end:
        return 0
    return f(st+2, end, s+'A')+f(st+5, end, s+'B')+f(st**2, end, s+'C')
print(f(4, 36, ' '))