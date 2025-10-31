alf='плюсёнок'
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                for x5 in alf:
                    for x6 in alf:
                        for x7 in alf:
                            sl = x1+x2+x3+x4+x5+x6+x7
                            if sl[0] in 'оёю':
                                if 'пё' not in sl and 'ёп' not in sl\
                                    and 'лё' not in sl and 'ёл' not in sl\
                                    and 'сё' not in sl and 'ёс' not in sl\
                                    and 'нё' not in sl and 'ён' not in sl\
                                    and 'кё' not in sl and 'ёк' not in sl:
                                    k+=1
print(k)
