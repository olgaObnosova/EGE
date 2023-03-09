a=8**740-2**900+7
k=0
while a>0:
    if a%2==0:
        k+=1
    a=a//2
print(k)