f=open('24St.txt').readline()
f=f.split('D')
maxx=0
for i in range(len(f)-1):
    l=len(f[i])+len(f[i+1])+1
    maxx=max(maxx,l)
print(maxx)
    
