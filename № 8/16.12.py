import itertools as t
sp=list(t.product('012345678', repeat = 5))
k=0
for x in sp:
    x= ''.join(x)
    if x[0]!='0' and x.count('5')==1:
        if '00' not in x and '11' not in x and '22' not in x and \
                '33' not in x and '44' not in x and \
                '55' not in x and '66' not in x and \
                '77' not in x and '88' not in x:
            k+=1
print(k)

