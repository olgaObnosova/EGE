with open('24_2942.txt') as f:
    f=f.readline()
f=f.replace('AB', '*')
f=f.replace('AC', '*')
k=maxx=0
for x in f:
    if x=='*':
        k+=1
        maxx=max(maxx, k)
    else:
        k=0
print(maxx)
