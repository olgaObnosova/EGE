f=[0]*97
g=[0]*97
f[0],f[1],f[2]=1,1,1
g[0],g[1],g[2]=2,-3,8
for i in range(3,97):
    if i%2!=0:
        f[i]=f[i-1]-i
        g[i]=f[i-1]-2*g[i-2]
    else:
        #print(i)
        f[i]=f[i-2]+g[i-1]+2
        g[i]=2*f[i-2]-2*g[i-1]
print(f[96])
