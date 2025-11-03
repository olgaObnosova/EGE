with open('24_9753.txt') as f:
    f=f.readline()
f=f.split('Y')
maxx=0
for i in range(len(f)):
    sp = 'Y'.join(f[i:i+151])
    maxx=max(maxx, len(sp))
print(maxx)