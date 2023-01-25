for i in range(100, 90, -1):
    for j in range(1, 102):
        a = i * '1' + j * '3'
        while '12' in a or '13' in a:
            a = a.replace('12', '21', 1)
            a = a.replace('31', '23', 1)
            a = a.replace('13', '23', 1)
    if '1' not in a:
        s = 0
        for x in a:
            s += int(x)
            if s == 404:
                print(i + j)
