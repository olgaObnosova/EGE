with open('st3.txt') as f:
    sp = [int(x) for x in f.readlines()]
minn=min(sp)
k=0
maxx=0
for i in range(len(sp)-1):
    if sp[i]%10==sp[i+1]%10 and ((sp[i]%3==0 and sp[i+1]%3!=0) \
        or (sp[i] % 3 != 0 and sp[i + 1] % 3 == 0)) \
            and sp[i]**2+sp[i+1]**2<=minn**2:
        k+=1
        maxx=max(maxx,sp[i]**2+sp[i+1]**2)
print(k)
print(maxx)