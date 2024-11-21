with open('24_17685.txt') as f:
    f=f.readline()
f=f.replace('++', '@')
f=f.replace('**', '@')
f=f.replace('+*', '@')
f=f.replace('*+', '@')
f=f.split('@')
f.sort(key=len, reverse=True)
print(f[:5])
sp=[]
for x in f:
    k=0
    st=''
    for i in range(len(x)-2):
        if not(x[i] in '*+' and x[i+1]=='0' and x[i+2] not in '+*'):
            k+=1
            st+=x[i]
        else:
            sp.append((len(st),st))
            k=0
            st=''
    sp.append((len(st), st))
sp.sort(reverse=True)
maxx=0
for x in sp[:5]:
    for i in range(len(x[1])):
        s=''
        for j in range(i, len(x[1])):
            s+=x[1][j]
            try:
                if eval(s)==0:
                    if len(s)>maxx:
                        maxx=max(maxx, len(s))
                        otv=s
            except:
                pass
print(maxx)
print(otv)






