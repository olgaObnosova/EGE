f=open("input.txt")

b=sorted([int(x) for x in f])

d=dict()
for z in range(len(b)-1):
    if (b[z+1]-b[z]) not in d:
        d[b[z+1]-b[z]]=1
    else:
        d[b[z + 1] - b[z]] = d[b[z + 1] - b[z]]+1
print(sorted(d.items(),key=lambda x:x[1],reverse=True))
