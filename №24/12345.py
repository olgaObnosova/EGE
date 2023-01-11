f=open('12345.txt').readline()
count=0
maxx=0
for i in range(len(f)):
    if f[i-1]!=f[i]:
        count+=1
        if count>maxx:
            maxx=count
    else:
        
        count=0
print(maxx)
print(len(min('qqq','w',key=len)))
