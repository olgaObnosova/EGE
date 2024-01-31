for i in range(1000, 10_000):
    a = str(i)
    s12 = int(a[0])+int(a[1])
    s23 = int(a[1]) + int(a[2])
    s34 = int(a[2]) + int(a[3])
    maxs = max(s12,s23,s34)
    mins = min(s12, s23, s34)
    sr = s12+s23+s34-maxs-mins
    r=str(sr)+str(maxs)
    if int(r)==613:
        print(i)
