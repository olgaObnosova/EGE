with open('fipi1.txt') as f:
    sp=[]
    for line in f:
        sp.append(int(line))
minn=min(sp)
k=0
mins=9999999
for i in range(len(sp)-1):
    if (sp[i]%111==minn or sp[i+1]%111==minn):
        k+=1
        mins=min(mins,sp[i]+sp[i+1])
print(k, mins)
