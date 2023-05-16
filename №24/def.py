with open('24(3).txt') as f:
    f=f.readline()
sp='ABC'
k=mx=0
for i in range(len(f)):
    if f[i] in sp and f[i+1] in sp:
        k+=1
        mx=max(mx,k)
    else:
        k=0
print(mx)