with open('24_2.txt') as f:
    f=f.readline()
f=f.replace('++','@')
f=f.replace('**','@')
f=f.split('@')
maxk=0
for x in f:
    k=0
    x=x.replace('+', '@')
    x = x.replace('*', '@')
    x=x.split('@')
    for y in x:
        if len(y)>0 and y[0]!='0':
            k+=1
            maxk=max(maxk, k)
        else:
            k=0
print(maxk)