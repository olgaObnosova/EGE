k=0
for i in range(2**4, 5**4):
    c=hex(i)
    if c[-1]=='c':
        k+=1
print(k)