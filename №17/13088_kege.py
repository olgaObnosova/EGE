with open('17_13088.txt') as f:
    sp=[int(x)for x in f]
maxx=0
for i in range(len(sp)):
    if sp[i]%100==17:
        maxx=max(maxx, sp[i])
cnt=maxs=0
for i in range(len(sp)-2):
    k=0
    if len(str(sp[i]))==4:
        k+=1
    if len(str(sp[i+1]))==4:
        k+=1
    if len(str(sp[i+2]))==4:
        k+=17
    if k==2 and (sp[i]%5==0 or sp[i+1]%5==0 or sp[i+2]%5==0) and \
            (sp[i]+sp[i+1]+sp[i+2]> maxx):
        cnt+=1
        maxs=max(maxs,sp[i]+sp[i+1]+sp[i+2])
print(cnt, maxs)

