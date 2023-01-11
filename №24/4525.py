f=open('4525.txt')
#f=f.readline()
a=[]
counttc=0 #кол-во точек
count=0 #длина последовательности #пять две три
maxx=0
for i in f:
    a.append(i)

a=''.join(a)
#print(a)
for i in range(len(a)):
    if a[i]=='.':
        #print(a[i])
        counttc+=1        
    count+=1
    if counttc>2:
        if count+counttc>maxx:
            maxx=count
        count=0
        counttc=0    
    #print(count)
    #print(counttc)
if count>maxx:
    maxx=count
print(maxx)
