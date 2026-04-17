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
    for i in range(len(x)-2): #123+46575+38965+05+76348+7867
        if not(x[i] in '*+' and x[i+1]=='0' and x[i+2] not in '+*'): # not (+05)
            k+=1
            st+=x[i]
        else:
            sp.append((len(st),st)) # [(12, 123+46575+38965), ()
            k=0
            st=''
    sp.append((len(st), st))
sp.sort(reverse=True)
print(sp[:2])
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