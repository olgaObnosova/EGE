with open('16_12') as f:
    f=f.readline()
    f=f.replace('RSQ',' RSQ ')
f=f.split()
print(f)
k=0
maxx=0
for i in range(len(f)):
    if f[i] == 'RSQ':
        k+=3
        maxx=max(maxx, k)
    elif f[i-1]=='RSQ' and len(f[i])>1 and f[i][0]=='R'and f[i][1]=='S':
        k+=2
        maxx = max(maxx, k)
    elif f[i-1]=='RSQ' and f[i][0]=='R':
        k+=1
        maxx = max(maxx, k)

    elif len(f[i])>1 and f[i][-2:]=='SQ' and f[i+1]=='RSQ':
        k=2
    elif f[i][-1]=='Q' and f[i+1]=='RSQ':
        k=1
    else:
        k=0
print(maxx)
ot='Q'+17 *'RSQ'+'RS' #17*3=51+3=54!
    if ot in f:
        print(1)