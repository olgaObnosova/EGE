print('p1,p2,p3,p4')
for p1 in 0, 1:
    for p2 in 0, 1:
        for p3 in 0, 1:
            for p4 in 0, 1:
                if ((p3 <= p1) <= (p4 or (1-p2))) == 0:
                    print(p1, p2, p3, p4)
