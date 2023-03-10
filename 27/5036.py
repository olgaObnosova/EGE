with open('primer.txt') as f:
    n = int(f.readline())
    sp = []
    s = k =otv= 0
    for line in f:
        sp.append(int(line))
        s+=int(line)
        if k<=n//2:
            otv += k * int(line)
        else:
            otv += (k-1) * int(line)
        k+=1
minn = float('inf')
levs = sp[0]
levs2=0
spis=[]
for i in range(len(sp)):
    if i<=n//2:
        prs = s - levs
        otv = otv - prs  + levs
        levs+=sp[i]
    else:
        prs = s - levs
        levs2+=sp[n//2-1-i]
        otv = otv - prs + levs-levs2
        levs += sp[i]
    spis.append((i,otv))
    print(spis)
    if otv<minn:
        minn=otv
        punkt=i
print(minn, punkt)