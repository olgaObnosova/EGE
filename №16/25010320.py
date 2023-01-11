f=[0]*130
g=[0]*130
f[0],f[1],f[2]=1,1,1
g[0],g[1],g[2]=1,1,1
for i in range(3,129):
    if i%2==0:
        g[i]=f[i-3]+f[i-2]
        f[i]=g[i]+f[i-1]
    else:
        f[i]=f[i-2]-2*g[i+1]
        g[i]=f[i+1]-g[i-1]
print(g[120])
        
