import itertools
countt=0
permit=set(itertools.product("НАСТЯ", repeat=7))
#print(permit)
for x in permit:
    x=''.join(x)
    if x.count('Н')==2 and x.count('А')>=1:
        countt+=1
        
        
print(countt)
