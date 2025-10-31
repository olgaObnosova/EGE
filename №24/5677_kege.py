with open('24_5677.txt') as f:
    f=f.readline()
e = 32*'DAD'
print(f.find(e))
print(f[19535:19541+100])
f=f.replace('DAD','*')
maxx=0
for x in range(len(f)):
    if  f[x]=='*':
        k+=1
        maxx = max(maxx, k)
    else:
        k=0
print(maxx)
print(maxx * 3)
