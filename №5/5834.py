sp = '0123456789abcdef'
for i in range(200000, 1, -1):
    h = hex(i)[2:]
    #print(h)
    if int(h,16) % 2 == 0:
        maxc = [int(x,16) for x in h]
        #print(maxc)
        maxc = max(maxc)
        #print(maxc)
        h = h + str(hex(maxc)[2:])
    else:
        h = h + '0'
    #print(h)
    for j in range(2):
        summa = [int(x,16) for x in h]
        summa = sum(summa)
        ost = summa % 16
        h = h + sp[ost]
        #print(h)

    maxc2 = [int(x,16) for x in str(h)]
    maxc2 = hex(max(maxc2))[2:]
    #print(maxc2)
    minc2 = [int(x,16) for x in str(h)]
    minc2 = hex(min(minc2))[2:]
    #print(minc2)
    if h.count(minc2)*5 == h.count(maxc2):
        print(i, h)
