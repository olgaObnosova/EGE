
def F(a,b):
    if a==0:
        return b
    else:
        return F(a//10,10*b+(a%10))
for i in range(100):
    print(F(i,0),i)
