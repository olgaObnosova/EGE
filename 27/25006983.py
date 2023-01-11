#4724
f=open('25006983A.txt')
sp=[0]*10000
n=int(f.readline())
k71=0
k=0
for line in f:
    line=int(line)
    if line%71:
        k71+=1
        if sp[line//71]>1 or sp[line]>1:
            k+=1

    sp[line]+=1
print(k)
'''
for x in sp:
    if x>=2:
        k+=(k71*x)
print(k, k71)
print(k71)
'''
