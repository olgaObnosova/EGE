with open('24_21.txt') as f:
    f=f.readline()
k=1
maxx=0
s=''
for i in range(len(f)-1):
    if f[i]!=f[i+1]: #XYW
        k+=1
        s+=f[i+1]
        if k>maxx:
            maxx = max(maxx, k)
            otv = s
    else:
        s=f[i]
        k=1
print(maxx)
print(otv)