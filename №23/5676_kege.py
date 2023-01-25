def f(start, stop):
    if start < stop:
        return 0
    elif start == stop:
        return 1
    else:
        return f(start - 3, stop) + f(start // 7, stop)


print(f(50, 1))
