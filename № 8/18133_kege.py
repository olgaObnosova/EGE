buk='ДИКМО'
k=0
for x1 in buk:
    for x2 in buk:
        for x3 in buk:
            for x4 in buk:
                for x5 in buk:
                    k+=1
                    x=x1+x2+x3+x4+x5
                    if x.count('М')==2 and "ММ" not in x:
                        print(k)
