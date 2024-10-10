sp=[0]*16
sp[1]=1
for i in range(2, 16):
    if i%2==0:
        sp[i]=sp[i-1] + sp[i-3]+sp[i//2]
    else:
        sp[i] = sp[i - 1] + sp[i - 3]
print(sp[15])