def s(n):
    st = set()
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            st.add(i)
            st.add(n//i)
    return sorted(st)
k = 0
for i in range(10_000_001,20_000_000):
    d = s(i)
    if len(d)<3:
        d = 0
    else:
        d = sum(d[-3:])
    if d!=0 and int(d**0.5)*int(d**0.5) == d:
        print(i,d)
        k+=1
    if k==5:
        break