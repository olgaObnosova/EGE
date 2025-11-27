with open('24_4602.txt') as f:
    f=f.readline()
k2=maxx2=0
for i in range(0, len(f)-1, 2):
    if f[i] in 'DCB' and f[i+1] in 'AO': # ADAAADADADA
        k2+=1
        maxx2 = max(maxx2, k2)
    else:
        k2=0
print(maxx2) #1
f=f.replace('A', '*')
f=f.replace('O', '*')
f=f.replace('B', '@')
f=f.replace('C', '@')
f=f.replace('D', '@')
f=f.replace('@*', '&')
k=maxx=0
for x in f:
    if x=='&':
        k+=1
        maxx=max(maxx, k)
    else:
        k=0
print(maxx) #174

