with open('4715.txt') as f:
    s = 0
    sp=[]
    for line in f:
        sp.append(int(line))
        if int(line)%33==0:
            a=int(line)
            while a>0:
                s+=a%10
                a=a//10
k=0
minn=9999999
for i in range(len(sp)-1):
    if sp[i]>s or sp[i+1]>s:
        k+=1
        minn=min(minn, sp[i]+sp[i+1])
print(k)
print(minn)