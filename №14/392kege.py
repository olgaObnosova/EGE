a=(2**345+8**65-4**130)*(8**123-2**89+4**45)
s=0
while a!=0:
    s+=a%8
    a=a//8
print(s)