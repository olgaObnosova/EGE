for x in '0123456789abcdefg':
    a = f'12346{x}17'
    b = f'7{x}171'
    if (int(a, 17) + int(b, 17)) % 16 == 0:
        print((int(a, 17) + int(b, 17)) // 16, x)
