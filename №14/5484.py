for x in '0123456789abcdefg':
    a = f'9759{x}'
    b = f'3{x}108'
    if (int(a, 17) + int(b, 17)) % 11 == 0:
        print(x, (int(a, 17) + int(b, 17)) // 11)
