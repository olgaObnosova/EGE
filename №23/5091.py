c = []


def f(start, count):
    global c
    if count == 17:
        c.append(start)
        return 0
        return c.append(start)
    else:
        if start > 0 and int(start ** 0.5) == start ** 0.5:
            return f(start - 1,count + 1) + f(start - 2,count + 1) + f(int(start ** 0.5),count + 1)
        else:
            return f(start - 1, count + 1) + f(start - 2, count + 1)

(f(113, 0))
print(len(set(c)))