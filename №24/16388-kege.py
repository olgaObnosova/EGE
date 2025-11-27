with open('24_16388.txt') as f:
    f=f.readline()
f=f.replace('KLMN', '****')
k=maxx=0
s=''
for x in f:
    if x=='*':
        k+=1
        s+=x
        if k>maxx:
            maxx=k
            otv =s
    else:
        k=0
        s=''
print(maxx)
print(f.index(otv))
print(f[2587378-10:2587378+10+180])
