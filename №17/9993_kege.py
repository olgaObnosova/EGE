def prost(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
with open('17_9993.txt') as t:
    sp=[int(x) for x in t]
#print(sp)
maxx=max([x for x in sp if abs(x)%100==17])
cnt=0
print(maxx)
maxpr=-float('inf')
for i in range(len(sp)-1):
    if sp[i]>0:
        p1 = prost(abs(sp[i]))
    else:
        p1=0
    if sp[i+1] > 0:
        p2 = prost(abs(sp[i+1]))
    else:
        p2=0
    if(p1+p2)==1 and (sp[i]+sp[i+1])%maxx==0:
        print(sp[i], sp[i + 1], sp[i] * sp[i + 1])
        cnt+=1
        maxpr=max(maxpr, sp[i]*sp[i+1])
print(cnt, maxpr)