sp=[0]*54_000
for i in range(54_000):
    if i<=5:
        sp[i]=1000
    else:
        sp[i]=i+3+sp[i-2]
print(3*sp[53079]-(sp[53077]+sp[53075]+sp[53073]))
