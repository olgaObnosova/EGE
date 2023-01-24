for x in '0123456789abcdef':
    a = int(f'8569{x}', 16) + int(f'12{x}48', 16)
    a = oct(a)[2:]
    k = 0
    for i in a:
        if int(i) % 2 == 0:
            k += 1
    if k <= 2:
        print(x, a)
