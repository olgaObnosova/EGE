with open('4365.txt') as f:
    sp = [int(x) for x in f]
min43 = float('inf')
for x in sp:
    if x % 43 == 0:
        min43 = min(x, min43)
maxx=0
k=0
for i in range(len(sp)-1):
    if (sp[i] + sp[i+1]) % min43==0 or\
            str(sp[i])[-1]==str(min43)[-1] or \
            str(sp[i+1])[-1] == str(min43)[-1]:
        k+=1
        maxx=max(sp[i], sp[i+1],maxx)
print(k)
print(maxx)