def dell(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            if prost(i):
                s.add(i)
            if prost(n//i):
                s.add(n//i)
    return list(s)
def prost(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return n
sh=0
for i in range(962333,96000100):
    sp=dell(i)
    #print(sp)
    s=0
    k=0
    for y in sp:
        
        
        if len(str(y))>1 and str(y)[-2]=='3':
                k+=1
                s+=y
    if k>=3:
        sh+=1
        print(s, i, sp)
        
    if sh==5:
        break
            
    
