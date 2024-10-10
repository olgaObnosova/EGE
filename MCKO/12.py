k=0
for i in range(8, 1000, 8):
    n=300
    s=i
    while s>0:
        s=s//6
        n=n//4
    if n==4:
        k+=1
print(k)