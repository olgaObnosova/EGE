k=0
for i in range(9, 10000, 9):
    s=i
    n=600
    while s>0:
        s=s//8
        n=n//3
    if n==7:
        k+=1
print(k)


