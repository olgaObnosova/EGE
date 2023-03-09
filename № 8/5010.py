import itertools as t
k=0
s=list(t.product('ПАРЕТ', repeat=8))
for x in s:
    x=''.join(x)
    if x.count('П')==2 and x.count('А')==2 and \
            x.count('Р') == 2 and x.count('Е')==1 and \
            x.count('Т') == 1:
        x = x.replace("Е", "*")
        x = x.replace("А", "*")
        x = x.replace("П", "@")
        x = x.replace("Р", "@")
        x = x.replace("Т", "@")
        if '**'  in x or "@@" in x:
            k+=1

print(k)