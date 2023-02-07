def f(start, stop):
    if start < stop:
        return 0
    elif start == stop:
        return 1
    else:
        return f(start - 8, stop) + f(start // 2, stop)


print(f(102, 43) * f(43, 5))
