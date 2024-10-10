with open('17_12471.txt') as f:
    sp=[int(x) for x in f]
maxx=0
cnt=0
s=0
for x in sp:
    if x%100==13:
        maxx=max(maxx, x)
for i in range(len(sp)-2):
    if ((sp[i]%2==0 and sp[i+1]%2==0 and sp[i+2]%2==0) \
            or (len(str(sp[i]))==2 or len(str(sp[i+1]))==2 \
        or len(str(sp[i+2]))==2)) and sp[i]+sp[i+1]+sp[i+2]<=maxx:
        cnt+=1
        s+=sp[i]+sp[i+1]+sp[i+2]
print(cnt)
print(s//cnt)

