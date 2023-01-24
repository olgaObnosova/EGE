for i in range(1, 100):
    s = 0
    a = 15 * '3' + 18 * '2' + i * '1'
    while '31' in a or '33' in a or '21' in a:
        if '31' in a:
            a = a.replace('31', '123')
        if '33' in a:
            a = a.replace('33', '211')
        if '21' in a:
            a = a.replace('21', '1')
    for x in a:
        s += int(x)
    if s > 24:
        print(i)
