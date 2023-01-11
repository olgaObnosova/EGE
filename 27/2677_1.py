f=open('2677.txt')
n=int(f.readline())
sp=[]
chet13=0
necet13=0
chet=0
necet=0
for i in range(5):
    sp.append(int(f.readline()))
for line in f:
    if sp[0]%2==0:
        chrt+=1
        if sp[0]%13==0:
            chet13+=1
    else:
        necet+=1
        if sp[0]%13==0:
            necet13+=1
    if line%13==0:
        if line%2==0:
            count+=necet
        else:
            count+=chet
    else:
        if line%2==0:
            count+=necet13
        else:
            count+=chet13
        
print(count)           
        
    
    
