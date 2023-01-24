print('x y z w')
for x in 0,1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                if (w and ((x<=y)==(y<=z))):
                    print(x,y,z,w)