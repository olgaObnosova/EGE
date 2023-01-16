for i in  '0123456789abcde':
    a = f'123{i}5'
    b = f'1{i}233'
    if (int(a,15) + int(b, 15)) % 14 == 0:
        print(i, (int(a,15)+int(b, 15))//14)