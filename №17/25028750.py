def tr(n):
    s=''
    while n>0:
        s+=str(n%6)
        n=n//6
    s=s[::-1]
    return s
maxx=k=mr=0
a = [int(x) for x in open('17_h.txt')]
for x in a:
    #r=tr(abs(x))
    if abs(x)%100==11:
        maxx=max(maxx,x)
print(maxx)
for i in range(len(a)-2):
    if (len(str(abs(a[i])))==4 and len(str(abs(a[i+1])))!=4 \
        and len(str(abs(a[i+2])))!=4) \
            or (len(str(abs(a[i])))!=4 and len(str(abs(a[i+1])))==4 \
        and len(str(abs(a[i+2])))!=4) \
            or (len(str(abs(a[i])))!=4 and len(str(abs(a[i+1])))!=4 \
        and len(str(abs(a[i+2])))==4):
        if (a[i]+a[i+1]+a[i+2]) % maxx==0:
            mr=max(mr, (a[i]+a[i+1]+a[i+2]))
            k+=1
print(k, mr)

