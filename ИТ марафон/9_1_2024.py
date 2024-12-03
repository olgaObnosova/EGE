with open('m9-1.txt') as f:
    f=f.readline().split('AA')
k=0
for x in f:
    if len(x)==34 and x[1]=='E':
        k+=1
print(k)
