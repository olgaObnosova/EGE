with open('24_15339.txt') as f:
    f=f.readline()
for x in 'ABC':
    f=f.replace(x, '*')
for x in '6789':
    f=f.replace(x, '&')
f=f.replace('&&', '**')
f=f.split('**')
maxx=0
for x in f:
    maxx=max(maxx, len(x))
print(maxx)