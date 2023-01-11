sp=[0]*1000
sp[21]=1
for i in range(22,63):
    sp[i]+=sp[i-i%10]
    if i%2==0:
        sp[i]+=sp[(i)// int(str(i//2)[0])]
    
    sp[i]+=sp[i-(int(max(list(str(i))))-int(min(list(str(i)))))]
print(sp[21:63])
    
