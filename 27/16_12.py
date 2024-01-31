with open('16_12') as f:
    n=int(f.readline())
    sp=[int(x) for x in f]
k=5000
s = maxx = otv = 0
sost=[[float('inf')]*2 for i in range(k)]
#print(sost)
for i in range(n):
    #print(sost, s)
    s+=sp[i]
    if sost[s%k][0] > s:
        sost[s%k][0] = s
        sost[s % k][1] = i
    if s%k==0:
        if s>maxx:
            maxx=s
            if i>otv:
                otv=i
    if (s-sost[s%k][0])>maxx:
        maxx = s-sost[s%k][0]
        if i - sost[s%k][1]>otv:
            otv = i - sost[s%k][1]
print(maxx, otv)
#print(sost)