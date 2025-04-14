with open('17_21416.txt') as f:
    sp=[int(x) for x in f]
smotr = sum([int(x) for x in sp if x<0])
maxx=k=0
for i in range(len(sp)-2):
    tr = sp[i:i+3]
    if max(tr)*min(tr)>smotr:
        k+=1
        maxx=max(maxx, (sum(tr)))
print(k, maxx)