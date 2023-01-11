#https://kompege.ru/variant?kim=25003483
count=0
maxx=999999999
for i in range(16015,48989+1):
    if (i%7==0 or i%11==0)and (i%9!=0 and i%12!=0 and i%13!=0):
        count+=1
        maxx=min(maxx,i)
print(count)
print(maxx)
