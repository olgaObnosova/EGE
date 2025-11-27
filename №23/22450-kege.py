def f(st, end):
    if st < end:
        return 0
    elif st == end:
        return 1
    elif str(st)[-1] == '0':
        return f(st - int(str(st)[0]), end) + \
            f(st - 2, end) + f(st // 2, end)
    elif int(str(st)[-1]) > 0:
        return f(st - int(str(st)[0]), end) + \
            f(st - int(str(st)[-1]), end) \
            + f(st // 2, end)
    return 0


print(f(47, 40) * f(40, 18) * f(18, 14))
