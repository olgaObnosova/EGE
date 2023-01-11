k=0
maxk=0
f=open('24st_1_23.txt').readline()
f=f.replace('CCA','*')
f=f.replace('CCO','*')
f=f.replace('CDA','*')
f=f.replace('DDA','*')
f=f.replace('DCA','*')
f=f.replace('CDO','*')
f=f.replace('DDO','*')
f=f.replace('DCO','*')
f=f.replace('FFA','*')
f=f.replace('FDA','*')
f=f.replace('DFA','*')
f=f.replace('CFA','*')
f=f.replace('FCA','*')
f=f.replace('FFO','*')
f=f.replace('FDO','*')
f=f.replace('DFO','*')
f=f.replace('CFO','*')
f=f.replace('FCO','*')
for i in f:
    if i=='*':
        k+=1
    else:
        maxk=max(maxk,k)
        k=0
print(maxk)
