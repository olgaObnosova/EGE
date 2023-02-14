rez = set()
def f(x,p):
    global rez
    if p == 11:
        rez.add(x)
    else:
        f(x-2,p+1)
        f(x*(-3),p+1)
f(91,0)
a=[]
for i in rez:
    if i <0:
        a.append(i)
print(len(a))
