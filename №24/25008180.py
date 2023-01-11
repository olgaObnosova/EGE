f=open('24_25008180.txt').readline()
maxk=0
k=0
for i in range(0,len(f),2):
    if (f[i]=='A' and f[i+1]=='B') or  (f[i]=='A' and f[i+1]=='C'):
        k+=1
    else:
        maxk=max(maxk,k)
        k=0
    
print(maxk)
