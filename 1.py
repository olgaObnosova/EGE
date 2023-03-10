sp=[]

n=135
for j in range(500):
    sp=set()
    for i in range(2, n+j*2):
        if (n+j*2)%i==0:
            sp.add(i)
    if len(sp)>0:
        print(sp, j)
        if len(sp)==3:
            break