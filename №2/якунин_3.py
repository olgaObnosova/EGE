print('y x z w')
for y in 0,1:
    for x in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not((x<=(y or w))==(z<=(x and y))):
                    print(y,x,z,w)