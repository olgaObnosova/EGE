with open('26_22127.txt') as f:
    n=f.readline()
    sp=[[int(x) for x in line.split()] for line in f]
vr =[0]*1440*60*1000
k=0
for x in sp:
    st, end = x
    for i in range(st, end+1):
        vr[i]+=1
for i in range(len(vr)):
    if vr[i]==0:
        print(i)


