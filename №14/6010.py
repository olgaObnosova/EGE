for x in '01234567':
    a = int(f'57a{x}9', 16)
    b = int(f'54{x}',8)
    c = a * b
    u = c
    s = 0
    while c > 0:
        s += c % 12
        c = c // 12
    if s == 40:
        print(u, x)
