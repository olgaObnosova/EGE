with open('17_23.10.23.txt') as f:
    sp=[int(x) for x in f]
k=maxx=maxc=0
for i in range(len(sp)):
    if sp[i]%100==19:
        maxc=max(maxc, sp[i])
print(maxc)
for i in range(len(sp)-2):
    if (len(str(sp[i]))==4 and len(str(sp[i+1]))==4 and len(str(sp[i+2]))!=4) or \
            (len(str(sp[i])) == 4 and len(str(sp[i + 2])) == 4 and len(str(sp[i + 1])) != 4) or \
            (len(str(sp[i+1])) == 4 and len(str(sp[i + 2])) == 4 and len(str(sp[i])) != 4):
            if sp[i]%3==0 or sp[i+1]%3==0 or sp[i+2]%3==0:
                if (sp[i]+sp[i+1]+sp[i+2])> maxc:
                    k+=1
                    maxx=max(maxx,sp[i]+sp[i+1]+sp[i+2])
print(k, maxx)

