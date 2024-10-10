print('x y z w')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if ((x or y) <=(y and z)) \
                        and ((w==x)or (w<= (not z))):
                    print(x, y, z, w)

