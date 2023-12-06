sp=[0]*3028
sp[1]=3
sp[2]=3
for i in range(3, 3028):
    sp[i] = 2*i+5+sp[i-2]
print(sp[3027]-sp[3023])