f=open('2508.txt')
f=f.readline()
count=1
maxc=0
sp=[]
#print(type(f[:10]))
for i in range(len(f)-1):
    if f[i]==f[i+1]:
        count+=1
        #sp.append(f[i])
    else:
        if count>=maxc:
            maxc=count
            sp.append((maxc,f[i]))
        count=1
print(sp)
