with open('24_21.txt') as f:
    f=f.readline()
print(f[:10])
k = 1
maxx = 0
s = ''
for i in range(len(f)-1): #XYXZXXY
    if f[i]!=f[i+1]:
        s+=f[i+1]
        k+=1
        if k>maxx:
            otv = s
            maxx=max(maxx, k)
    else:
        k = 1
        s=f[i+1]
print(maxx)
print(otv)