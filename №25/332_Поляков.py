def f(n):
    sp = set()
    global M
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sp.add(i)
            sp.add(n // i)
    if len(sp)>0:
        M = (min(sp)+max(sp))
    else:
        M = 0
    return sorted(sp)
sp=[]
k=0
for n in range(1,800000):
    y=f(n)
    sp.append(y)
    if M%10==2:
        k+=1
        print(M,n)
        if k==5:
            break
# 12 20
# 12 27
# 12 35
# 22 40
# 22 57

