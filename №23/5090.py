def f(start, stop):
    if start < stop or start == 20:
        return 0
    elif start == stop:
        return 1
    else:
        return f(start - 1, stop) + f(start - 2, stop)


print(f(27, 17))
