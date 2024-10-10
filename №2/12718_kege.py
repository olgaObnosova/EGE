print('k m l n')
for k in 0,1:
    for m in 0, 1:
        for l in 0, 1:
            for n in 0, 1:
                if ((not(k<=m)) and (k or n) or (l<=n))==0:
                    print(k, m, l,n)
