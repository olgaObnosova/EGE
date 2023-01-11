for x in '0123456789abcde':
    if (int('123'+x+'5',15)+int('1'+x+'233',15))%14==0:
        print(x)
        print((int('123'+x+'5',15)+int('1'+x+'233',15))/14)
        break

