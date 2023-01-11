sp=[0]*3520
sp[1]=1
for i in range(2,3520):
    sp[i]=(2*i-1)*sp[i-1]
print(sp[3516]/sp[3513])
