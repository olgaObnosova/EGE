f=[0]*1201
g=[0]*1550
for i in range(1501, 1550):
    g[i]=5
for i in range(1500,0,-1):
    g[i]=g[i+1]+g[i+2]+1
for i in range(1201):
    if i<=4:
        f[i]=1
    else:
        f[i]=f[i-1]+f[i-3]+g[i-2]
print((f[1200]+g[100])%10000)