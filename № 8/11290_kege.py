alf='0123456789abcdef'
k=0
for x1 in alf:
    for x2 in alf:
        for x3 in alf:
            for x4 in alf:
                sl = x1+x2+x3+x4
                if (sl[0]!='0' and sl.count('9')==1):
                    sl = sl.replace('0', '*')
                    sl = sl.replace('2', '*')
                    sl = sl.replace('4', '*')
                    sl = sl.replace('6', '*')
                    sl = sl.replace('8', '*')
                    sl = sl.replace('a', '*')
                    sl = sl.replace('c', '*')
                    sl = sl.replace('e', '*')
                    sl = sl.replace('1', '@')
                    sl = sl.replace('3', '@')
                    sl = sl.replace('5', '@')
                    sl = sl.replace('7', '@')
                    sl = sl.replace('9', '@')
                    sl = sl.replace('b', '@')
                    sl = sl.replace('d', '@')
                    sl = sl.replace('f', '@')
                    if '**' not in sl and '@@'  not in sl:
                        k=k+1
print(k)