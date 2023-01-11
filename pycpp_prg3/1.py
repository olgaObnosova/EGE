f=open('input.txt')
f2=open('output.txt','w')
fl=0
och=[]
for line in f:
    if line[0]=='+':
        och.append(line[1:])
    elif line[0]=='-' and len(och)>0:
        och.pop(0)
    else:
        fl=1
if fl:
    f2.write('ERROR')
elif len(och)==0:
    f2.write('EMPTY')
else:
    och=''.join(och).replace('\n',' ')
    
    f2.write(och)
f2.close()
