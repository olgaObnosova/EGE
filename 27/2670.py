f = open('2670B.txt')
n = int(f.readline())
count = 0
minn_final=999999999
for i in range(n):
    x, y, z = map(int, f.readline().split())
    maxx = max(x, y,z)
    minn = min(x,y, z)
    sr = (x+y+z)-maxx-minn
    count += maxx
    
    if abs(maxx-sr)%4 > 0:
        minn_final = min(abs(maxx-sr), minn_final)
    if abs(maxx-minn)%4 > 0:
        minn_final = min(abs(maxx-minn), minn_final)

if count % 4 != 0:
    print(count)
else:
    print(count - minn_final)
