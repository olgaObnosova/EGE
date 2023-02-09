k = 0
for i in range(3, 51):
    a = '>' + i * '1' + i * '2' + i * '3'
    while '>1' in a or '>2' in a \
            or '>3' in a:
        if '>1' in a:
            a = a.replace('>1', '22>3', 1)
        if '>2' in a:
            a = a.replace('>2', '2>', 1)
        if '>3' in a:
            a = a.replace('>3', '11>2', 1)
    if (a.count('1') + a.count('2') * 2 + a.count('3') * 3) % 7 == 0:
        k += 1
print(k)
