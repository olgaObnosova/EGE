def f(start, end, flags):
    if flags.count(start) > 1:
        return 0
    if start > 40 or start < -40:
        return 0
    if start == end:
        return 1
    else:
        flags1 = flags.copy()
        flags2 = flags.copy()
        flags1.append(start + 2)
        flags2.append(start - 3)
        return f(start + 2, end, flags1) + f(start - 3, end, flags2)
print(f(1, 30, [1]))