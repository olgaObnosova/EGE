print('x y z w')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((x and not z) or(y==z) or not w)==0:
                    print(x, y, z, w)
