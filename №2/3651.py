print('a b c')
for a in 0,1:
    for b in 0, 1:
        for c in 0, 1:
            if a==b or b<=c:
                print(a,b,c)