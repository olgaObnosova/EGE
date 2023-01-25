sp=[0]*1000
sp[0]=1
sp[1]=1
for i in range(2,1000-2):
    if i%2==0:
        sp[i]=3+sp[i//2-1]
    else:
        sp[i]=0
for i in range(len(sp)):
    if sp[i]==19:
        print(i)