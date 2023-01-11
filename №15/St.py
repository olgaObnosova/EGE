'''
def r(x,a):
    return (x&85!=0 or x&54==0 or x&a!=0)
for a in range(100):
    for x in range(1000):
        
        if r(x,a):
'''          

for a in range(100):
    f=1
    for x in range(1000):
        f*=(x&85!=0 or x&54==0 or x&a!=0)
    if f:
        print(a)
        break
  
