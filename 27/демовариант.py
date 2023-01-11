
f = open('27_Ad.txt')
n=int(f.readline())
sp=[]
for line in f:
    a,b = map(int, line.split())
    sp.append([a,b//36+int(bool(b%36))])
pay=[0]*n
summl=summr=0
print(sp)

for i in range(1,n):
    pay[0]+=sp[i][1]*(sp[i][0]-sp[0][0])
    summr+= sp[i][1]#количество пробирок справа
#print(pay)
print(summr)
for i in range(1,n):
    summl+= sp[i-1][1]#количество пробирок слева
    pay[i]=pay[i-1]-summr*(sp[i][0]-sp[i-1][0])+summl*(sp[i][0]-sp[i-1][0])
    summr-=sp[i][1]
print(min(pay))
