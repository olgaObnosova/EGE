k = 0
for x1 in '1234567':
    for x2 in '01234567':
        for x3 in '01234567':
            for x4 in '01234567':
                for x5 in '01234567':
                    a = x1 + x2 + x3 + x4 + x5
                    if a.count('6')==1 and '16' not in a and \
                            '61' not in a and'36' not in a and \
                            '63' not in a and'56' not in a and \
                            '65' not in a and'76' not in a and \
                            '67' not in a:
                        k+=1
print(k)



