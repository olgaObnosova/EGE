with open('17_23757.txt') as f:
    sp=[int(x) for x in f]
minn = float('inf')
for x in sp:
    if 9<x<100:#len(str(abs(x)))==2
        minn = min(minn, x)
cnt=maxx=0
for i in range(len(sp)-1): # 1 2 3 4 5
    p1 = 9 < sp[i] < 100 # T F / 1 0
    p2 = 9 < sp[i+1] < 100# T F/1 0
    if p1+p2==1 and (sp[i]+sp[i+1]) % minn==0:
        cnt+=1
        maxx = max(maxx, sp[i]+sp[i+1])
print(cnt, maxx)
