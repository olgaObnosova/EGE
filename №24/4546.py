f=open('24_4546.txt').readline()
f=f.replace('AAA','*')
f=f.replace('ABA','*')
f=f.replace('ACA','*')
f=f.replace('CAC','*')
f=f.replace('CBC','*')
f=f.replace('CCC','*')
c=1
maxc=0
for x in f:
    if x=='*':
        c+=1
    else:
        maxc=max(maxc,c)
        c=1
print(maxc)
