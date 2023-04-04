kor=range(1,22)
kub=[]
for x in kor:
    kub.append(x**3)
with open('5179.txt') as f:
    sp=[]
    maxx=0
    for line in f:
        sp.append(int(line))
        if int(line) in kub:
            maxx = max(maxx, int(line))
for i in range(len(sp)-2):
    sm= sp[i]+sp[i+1]+sp[i+2]
    f=abs(maxx-sm)
    if f%2==0 and int(f**0.5)==f**0.5:
        k+=1
        if sp[i]+sp[i+1]+sp[i+2]> mx:

