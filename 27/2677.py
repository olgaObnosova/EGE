#2677
f=open('B2677.txt')
a=[]
c=0
k13c, k13n, ch,n,k=0,0,0,0,0
m=int(f.readline())
#print(n)
for i in range(5):
    a.append(int(f.readline()))
#print(a)
for line in f:
    line=int(line)
    if a[0]%2==0:
        ch+=1
        if a[0]%13==0:
            k13c+=1
    else:
        n+=1
        if a[0]%13==0:
            k13n+=1
    if line%13==0:
        if line%2==0:
            k+=n
        else:
            k+=ch
    else:
        if line%2==0:
            k+=k13n
        else:
            k+=k13c
    for i in range(4):
        a[i]=a[i+1]
    a[4]=line
    #print(a)
    
print(k)
        
            
        


'''
print('x','y','z','w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not ((x and z) or ((w<=x)==(z<=y))):
                    print(x,y,z,w)
''' 
'''
#2790
from itertools import *
b=[]
for x in product('ЬСОНЕ',repeat=4):
    a=''.join(x)
    b.append(a)
print(b)
#print(([''.join(x) for x in product('ЬСОНЕ',repeat=4)][99]))
#print([*map(''.join, product('ЬСОНЕ',repeat=4))][99])
'''


#4256

'''for x in permutations("КУСАТЬ",5):
    b=str("".join(x))
    if ("СУК"  not in b) and  b[0]!="Ь":
        e+=1
print(e)'''
#print(len([str("".join(x)) for x in permutations('КУСАТЬ',5) if ("СУК"  not in str("".join(x))) and str("".join(x))[0]!="Ь"]))


#4255
'''b=0
for i in range(1,100000):
    if len((oct(i))[2:])==4 and int(oct(i)[2:])%4==0:
        b+=1

print(b)'''
