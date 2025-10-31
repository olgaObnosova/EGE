def f(n):
    n=str(n) #123456
    k1 = int(n[0])+int(n[1])
    k2 = int(n[2]) + int(n[3])
    k3 = int(n[4]) + int(n[5])
    r = str(k1) + str(k2) + str(k3) #строка
    r = bin(int(r))[2:]
    if int(r, 2)%2==0:
        r=r+'0'
    else:
        r=r+'1'
    r=int(r, 2)
    return r
for i in range(100_000, 1_000_000):
    if str(i)[-2]=='9' and str(i).count('2')>0:
        if f(i)==1519:
            print(i)
            break
