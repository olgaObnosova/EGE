sp=[0]*2210
for i in range(2210):
    if i<2025:
        sp[i]=i**2
    if 2025<=i<2050:
        sp[i]=2*sp[i-1]-sp[i-2] + i
    if 2050<=i<=2100:
        sp[i]=sp[i-1]+2*sp[i-2]+3*sp[i-3]
    if i>2100:
        sp[i]=2*sp[i-1]+sp[i-2]+i
print(sp[2020]+sp[2200])