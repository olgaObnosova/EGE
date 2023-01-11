f=open('27_B_25006891.txt')
n=int(f.readline())
sp=[10**9]*17
spol=0
sotr=0
for line in f:
    line=int(line)
    if abs(line)<sp[abs(line)%17]:
        sp[abs(line)%17]=abs(line)
    if line>0:
        spol+=line
    else:
        sotr+=line
    
print(sp)
print(spol-sp[spol%17])
print(sotr)


