def d(n):
    s=set()
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            s.add(i)
            s.add(n//i)
    if len(s)>=2:
        return True
    else:
        return False
for k in range(1,10):
    M=7_000_000+k
    kor=M**0.5
    if not(kor==int(kor) and d(kor)):
            print(k)
