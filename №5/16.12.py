
for i in range(1, 100):
    n=
    if i %2==0:
        n = n +n[-2:]
    else:
        n = '1' + n +'0'
    r = int(n,2)

    #print(r)
    if r<100:
        print(i)


