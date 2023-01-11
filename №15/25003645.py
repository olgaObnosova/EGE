#https://kompege.ru/variant?kim=25003645
q=[]
for i in range(29,48):
    q.append(i)
mn={48,52,56}
for a in range(1,100):
    f=1
    for x in range(1,1000):
        f*=(x%3==0 or x in mn or abs(x-50)>7 or x in q or x&a==0)
    if f:
        print(a)
    
