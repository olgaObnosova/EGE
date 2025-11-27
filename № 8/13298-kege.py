import itertools as t
sp=[]
comb = list(t.product('АВИКПРЧЫ', repeat =5))
k=0
for i in range(0, len(comb)):
    k+=1
    if k%5!=0:
        x=''.join(comb[i])
        sp.append((x, i))
print(comb[:10])
print(sp[:10])
cnt=0
for x in sp:
    cnt+=1
    sl, k = x
    if 'А' not in sl and 'И' not in sl\
            and 'Ы' not in sl\
        and len(set(sl))==len(sl):
        print(sl, k, cnt)

