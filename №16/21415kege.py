sp=[0]*2130
for i in range(1, 2130):
    if i<=5:
        sp[i]=1
    else:
        sp[i]=i+sp[i-2]
print(sp[2126]-sp[2122])

