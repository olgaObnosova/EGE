for x in '0123456789abcde':
    if (int('123{}5'.format(x),15)+int('1{}233'.format(x),15))%14==0:
        print(x)
        print((int('123{}5'.format(x),15)+int('1{}233'.format(x),15))/14)
        break
