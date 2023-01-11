s=[0]*16
s[0],s[1],s[2]=1,1,1
for i in range(3, 16):
    if i%2==0:
        s[i]=2*s[i-1]-s[i-2]
    else:
        s[i]=s[i-1]-2*s[i-2]-3
print(s)
