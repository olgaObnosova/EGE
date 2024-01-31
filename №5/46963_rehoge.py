for i in range(39, 40):
    n = bin(i)[2:]
    print(n)
    k1 = k0 = 0
    for j in range(len(n)):
        if j%2!=0 and n[j]=='1':
            k1+=1
        elif j%2==0 and n[j]=='0':
            k0+=1
    r = abs(k1-k0)
    print(r, k1, k0)
    if r==5:
        print(i)

