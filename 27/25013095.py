with open('25013095_B.txt') as f:
    n = int(f.readline())
    sp,k,s=[],0,0
    for line in f:
        k+=1
        line=int(line)
        if line%2==0:
            s+=line
            sp.append((s, k))   
        else:
            sp.append((0, k))
maxx=0
#print(sp) 
sp=sp[::-1]
t=0
for i in range(len(sp)-1):
    t+=1
    for j in range(i+1,len(sp)):
        if abs((sp[i][0]-sp[j][0])) %16==0:
            if abs(sp[i][0]-sp[j][0])>maxx:
                maxx = abs(sp[i][0]-sp[j][0])
                a=i
                b=j
    if t==15:
        break
#print(sp)           
print(maxx %16)
print(a)
print(b)
print(abs(a-b))
