a=2**51+2**40+2**35+2**17-2**5
s=set()
while a>0:
    s.add(a%16)
    a=a//16
print(len(s))
