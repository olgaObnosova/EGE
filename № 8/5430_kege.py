k=0
for x1 in '123456789':
    for x2 in '0123456789':
        for x3 in '0123456789':
            for x4 in '0123456789':
                for x5 in '0123456789':
                    for x6 in '0123456789':
                        for x7 in '0123456789':
                            for x8 in '0123456789':
                                for x9 in '0123456789':
                                    a = set(x1+x2+x3+x4+x5+x6+x7+x8+x9)
                                    if len(a)>=3:
                                        k+=1

print(k)