def f(start, end, flags):
    if start > end:
        return 0
    elif start == end and flags <= 3:
        return 1
    else:
        return f(start + 2, end, flags) + f(start * 3, end, flags + 1) + f(start * 5, end, flags + 1)
print(f(2, 200, 0))