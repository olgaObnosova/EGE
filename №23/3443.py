def f(x, y):
    global ymin
    if x == 227:
        if y < ymin:
            ymin = y
    if x * 3 <= 227:
        f(x * 3, y + 1)
    if x + 5 <= 227:
        f(x + 5, y + 1)
    elif x + 1 <= 227:
        f(x + 1, y + 1)
ymin = 10000
f(1, 0)
print(ymin)
