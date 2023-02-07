m = 0
for i in range(203):
    a = i * '1' + '2' + (203 - i) * '1'
    while '111' in a or '222' in a:
        if '111' in a:
            a = a.replace('111', '22', 1)
        else:
            a = a.replace('222', '11', 1)
    if len(a) > m:
        m = len(a)
        b = a
print(b)
