for x in '0123456789abcdefg':
    a = int(f'10{x}0', 17)
    b = int(f'f0{x}ff', 17)
    if (a + b) % 13 == 0:
        print(x, (a + b) // 13)
