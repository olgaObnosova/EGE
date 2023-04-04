for j in range(10):
    for i in range(4):
        for k in range(4):
            a = j*(i * '1' + k * '0')
            if len(a) == 40:
                while '0<' in a or '1<' in a:
                    if '11<' in a or '10<' in a:
                        if '11<' in a:
                            a = a.replace('11<', '<3', 1)
                        else:
                            a = a.replace('10<', '<2', 1)
                    else:
                        if '00<' in a:
                            a = a.replace('00<', '<0', 1)
                        if '01<' in a:
                            a = a.replace('01<', '<1', 1)
                s = 0
                for x in a:
                    s += int(x)
                print(len(a), s)
