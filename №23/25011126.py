def fun(s,f):
    if s==f:
        return True
    if s<10:
        return False
    
    return fun(s//10 +s%10,f)  or fun((s//10)*(s%10),f)
k=0
for i in range(10,100):
    if fun(i,8):
        k+=1
print(k)
    
