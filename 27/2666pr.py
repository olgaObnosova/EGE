with open('2666_A.txt') as f:
    n=int(f.readline())
    maxx=0
    sp=[int(x) for x in f]
for i in range(len(sp)-1):
    for j in range(i+1, len(sp)):
        if (sp[i]* sp[j])%6==0:
            maxx=max(maxx, sp[i]*sp[j])
print(maxx)