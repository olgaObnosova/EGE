with open('24_1302.txt') as f:
    f=f.readline()
f=f.replace('XZZY', '*') #aaaaaXZZYaaa
f=f.split('*') #[Xaaaaa, aaa]
maxx=0
for x in f:
    if len(x)>maxx:
        maxx=max(maxx, len(x))
        otv=x
print(maxx+6)
print(f.index(otv))
print(len(f))# надо смотреть начало и конец