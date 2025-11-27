sp=[0]*2030
for i in range(2030):
    if i<110:
        sp[i]=i
    else:
        sp[i]=i+sp[i-1]
print(sp[2025]-sp[2021])