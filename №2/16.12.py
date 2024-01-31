print('x y z w')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if not( y and (x or z) or not(y or z) or w):
                    print(x, y, z,w)
