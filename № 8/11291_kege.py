alf = '012345'
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        for x7 in alf:
                            sl = x1+x2+x3+x4+x5+x6+x7
                            if  sl[0]!='0' and sl.count('2')==1 \
                            and '02' not in sl and '20' not in sl and '42' not in sl and '24' not in sl:
                                k = k+1
print(k)