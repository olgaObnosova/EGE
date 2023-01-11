import itertools
C = []
k=0
permit=list(itertools.permutations("СВЕТЛАНА", r=8))
print(permit[1])
for x in permit:
    flag=1
    for i in range(len(x)-1):
        if x[i]==x[i+1]:
            flag=0
    if flag:
        #print(x)
        k+=1
print(k//2)
