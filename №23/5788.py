c = 0

def f(start, end):
    global c
    if start[0] > end[0] or start[1] > end[1]:
        return 0
    elif start[0] == end[0] and start[1] == end[1]:
        c += 1
        return 1
    else:
        return f([start[0] + 1, start[1]], end) + f([start[0] * 2, start[1]], end) + f([start[0], start[1] + 3], end)
print(f([1,0], [17, 27]))
