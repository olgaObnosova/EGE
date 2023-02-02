with open('5399.txt') as f:
    n, m = map(int, f.readline().split())
    sp = [int(x) for x in f]
sp.sort()
sp=sp[::-1]
otw=[]
otw2=[]
k = i = 0
while len(sp)>1 and (sp[i]+sp[len(sp)-1-i])<=m:
        otw.append((sp[i]+sp[len(sp)-1]))
        sp.pop(0)
        sp.pop(len(sp)-1)
        while len(sp)>1 and (sp[i]+sp[len(sp)-1-i])>m:
            otw2.append(sp[i])
            sp.pop(i)

print(len(otw))
print(sum(otw2))


