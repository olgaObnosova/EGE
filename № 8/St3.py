import itertools
C = []
k=0
count=0
zapr=['МР','СМ','МС','РМ','ХМ','РС','СР','РХ',\
      'МХ','АА','АО','ОА','ОО','РМ','ХР',\
      'ХС','СХ']
permit=set(itertools.permutations("РОСОМАХА", r=8))
for x in permit:
    x=''.join(x)
    f=1
    for  l in x:
        if l in zapr:
            f=0
    if f: count+=1
        
print(count)
