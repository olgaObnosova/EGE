import string as s
with open('24_887.txt') as f:
    f=f.readline()
alf = s.ascii_uppercase
print(alf)
sp=[0]*len(alf)
for i in range(len(f)):
    if f[i]=='X':
        ind = alf.find(f[i+1])
        sp[ind]+=1
print(sp.index(1618)) #1618
print(alf[20])