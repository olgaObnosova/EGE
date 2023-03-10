print('x y z w')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (((x<=w) and ((1-y)<=z))\
                        <=((z==x)or (w and(1-y)))) ==0:
                    print(x,y,z,w)
