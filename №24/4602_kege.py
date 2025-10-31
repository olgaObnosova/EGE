with open('24_4602.txt') as f:
    f=f.readline()
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
print(maxx)
