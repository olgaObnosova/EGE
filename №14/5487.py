for x in '0123456789a':
    a = f'3364{x}'
    b = f'{x}7946'
    c = f'55{x}87'
    if (int(a, 11) + int(b, 12)) == int(c, 14):
        print(int(c, 14))
