import time as t
def f(n):
    s=set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    return s
# sp=[]
# for i in range(159264873, 973146286):
#     if i**0.5==int(i**0.5):
#         t = f(i)
#         sp.append((i, t))
# print(sp)
def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
sp=[]
start = t.time()
for i in range(12621, 31196, 2000):
    if not(pr(i)):
        sp.append(i**2)
for i in range(0, len(sp)):
        print(sp[i], len(f(sp[i])))
end= t.time()
print(end-start)
print(t.process_time())
