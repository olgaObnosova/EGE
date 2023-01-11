#https://kompege.ru/variant?kim=25003483
f=open('24_25003483.txt')
maxx=0
f=f.readline().split('XZZY')
for x in f:
    maxx=max(len(x),maxx)
    
print(maxx)
