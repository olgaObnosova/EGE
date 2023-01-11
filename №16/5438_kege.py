sp= [0]*1031
sp[1] = 2
for i in range (2,1031):
    sp[i] = sp[i-1] * ((3 ** (i % 5))/ (3** (i % 7)))
print(sp)
print(sp[1025], sp[1030])