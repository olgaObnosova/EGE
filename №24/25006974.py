a='asdffHJJJLkfjjjjjjjjjjjLkfj'
sp=['0']*len(a)
for i in range(1,len(a)-1):
    if (a[i-1])<(a[i]) and (a[i+1])<(a[i]):
        sp[i]='1'
sp=''.join(sp)
sp=sp.split('1')
print(len(max(sp)))

        
    
    
