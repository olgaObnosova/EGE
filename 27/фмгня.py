f=open('27-ASt.txt')
sp=[]
n=int(f.readline())
for line in f:
    sp.append(int(line))
maxs=0
s=0
k=0
for i in range(n):   
    if sp[i]%2!=0:
        k+=1
   
    if k==441:
        break
    s+=sp[i]
print(s)

    
    
 
         
            
            
        
