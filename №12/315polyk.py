def f(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
k=0
for i in range(10, 1_00):
    st='1'+i*'0'
    print(i)
    while '10' in st:
        st = st.replace('10', '001', 1)
        st = st.replace('1', '01', 1)
    if f(len(st)):
        k+=1
print(k)