def f(start, stop, k):
    if start > stop:
        return 0
    elif start == stop and (k[-1]=='A' or k[-1]=='C'):
        return 1
    return f(start + 2, stop, k+'A') + \
        f(start + 3, stop, k+'B') + f(start * 2, stop, k+'C')


print(f(3, 20, ''))