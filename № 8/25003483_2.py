x='ВИШНЯ'
k=0
for a in x:
    for b in x:
        for c in x:
            for d in x:
                for e in x:
                    for f in x:
                        t=a+b+c+d+e+f
                        if t.count('В')<=1 and t[0]!='Ш' \
                           and t[5]!='И' and t[5]!='Я':
                            k+=1
print(k)
