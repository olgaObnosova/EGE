with open('17st_01_04.txt') as f:
    sp=[int(x) for x in f]
cnt = 0
maxs = 0
kv = len([x for x in sp if abs(x)%10==3 \
          and len(str(abs(x)))==4])**2
print(kv)
for i in range(len(sp)-3):
    maxx = max(sp[i:i+3])
    minn = min(sp[i:i+3])
    maxx2 = sum(sp[i:i+3])-maxx-minn
    if (maxx2+maxx)>kv:
        cnt+=1
        maxs=max(sum(sp[i:i+3]), maxs)
print(cnt, maxs)


