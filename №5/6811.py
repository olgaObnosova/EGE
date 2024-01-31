for i in range(1,100):
    s=''
    n=i
    while n!=0:
        s+=str(n%3)
        n=n//3
    N=s[::-1]
    if i%3==0:
        N='1'+s+'02'
    else:
        s1=''
        ost=(i%3)*4
        n1=ost
        while n1 != 0:
            s1 += str(n1 % 3)
            n1 = n1 // 3
        N = N+s1[::-1]
    r=int(N,3)
    if r < 199:
        print(i)

