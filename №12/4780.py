for i in range(251, 500):
    a = '5' * i
    while '55555' in a:
        a = a.replace('55555','88',1)
        a = a.replace('888', '555', 1)
    print(a, a.count('5'), i)