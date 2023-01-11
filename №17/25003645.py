#https://kompege.ru/variant?kim=25003645
sp=[]
for i in range(8**3,8**4):
    sp.append(i)
count=0
maxs=0
for i in range(1,len(sp)-1):
    if (sp[i]%11==0 or sp[i]%13==0) and ((sp[i+1]%11==0 or sp[i+1]%13==0)\
       or (sp[i-1]%11==0 or sp[i-1]%13==0)):
        count+=1
        maxs=max(maxs,sp[i])
print(count, maxs)      
