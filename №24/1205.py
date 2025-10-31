with open('24_1205.txt') as f:
    f=f.readline()
f=f.replace('G', '*')
f=f.replace('W', '*')
f=f.replace('P', '*')
k=maxx=0
for x in f:
    if x!='*':
        k+=1
        maxx=max(maxx, k)
    else:
        k=0
print(maxx)