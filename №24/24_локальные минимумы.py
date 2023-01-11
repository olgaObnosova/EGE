f=open('string.txt')
a=[]
a=f.readline()
ans=[]
maxx=0
for i in range(len(a)-1):
    print(a[i-1],i)
    break
    if ord(a[i-1])>=ord(a[i])<=ord(a[i+1]):
        ans.append(int(i))
for i in range(len(ans)-1):
    if abs(ans[i]-ans[i+1])>=maxx:
        maxx=abs(ans[i]-ans[i+1])
print(maxx)
