k=0
for i in range(128, 256,2):
    n=oct(i)[2:]
    s=0
    for x in n:
        s+=int(x)
    if s%2==0:
        n=n[:-1]+'2'
    else:
        n='1'+ n[1:]
    if int(n,8)>=100:
        k+=1
print(k)
print((640000*1920*1080)/(2560*1440))