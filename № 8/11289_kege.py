alf = '012345678'
k = 0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        for x7 in alf:
                            sl = x1+x2+x3+x4+x5+x6+x7
                            if  sl[0]!='0' and sl.count('2')==0 and len(sl)==len(set(sl)):
                                sl = sl.replace('0', '*')
                                sl = sl.replace('4', '*')
                                sl = sl.replace('6', '*') #468 - ***
                                sl = sl.replace('8', '*')
                                sl = sl.replace('1', '@')
                                sl = sl.replace('3', '@')
                                sl = sl.replace('5', '@')
                                sl = sl.replace('7', '@')
                                if '**' not in sl and '@@' not in sl:
                                    k += 1
print(k)