def f(st, end):
    if st==end:
        return 1
    elif st>end:
        return 0 #123 _132
    if int(str(st)[-2]) < int(str(st)[-1]):
        return f(st+1, end)\
            + f(int(str(st)[:-2]+str(st)[-1]+str(st)[-2]), end)
    else:
        return f(st+1, end)
print(f(101, 154))