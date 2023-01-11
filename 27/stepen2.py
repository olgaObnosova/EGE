def stepen(n):
    k=0
    while n>1:
        if n%2==0:
            k+=1
            n=n//2
        else:
            return k        
    return k
print(stepen(7))
