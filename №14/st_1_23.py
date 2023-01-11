for x in '0123456789abcdef':
    a='1'+x+'bad'
    b='2c'+x+'fe'
    if (int(a,16)+int(b,16))%15==0:
        print(x)
        print((int(a,16)+int(b,16))/15)
