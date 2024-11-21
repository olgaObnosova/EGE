def sem(n):
    s = ''
    while n != 0:
        s += str(n % 7)
        n = n // 7
    return s[::-1]


maxx = 0
for i in range(1, 10000):
    n = sem(i)  # строка
    if n.count('2') % 2 == 0:
        n = n[:-3]+'555' # заменит последние 3 на 555
    else:
        n = '1' + n
    r = int(n, 7)
    if r < 3799:
        maxx = max(maxx, i)
print(maxx)
