sp=[0]*4965
for i in range(4965, 0, -1):
    if i<=3:
        sp[i]=i-1
    elif i%2==0:
        sp[i]=sp[i-2]+i//2-sp[i-4]
    else:
        sp[i]=sp[i-1]*i+sp[i-2]
print(sp[4952]+2*sp[4958]+sp[4964])