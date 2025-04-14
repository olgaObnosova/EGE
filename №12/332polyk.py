def f(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
for i in range(1000):
    #print(i)
    st='0'+'1'*i+'2'*i+'0'
    while '00' not in st:
        st=st.replace('02', '101', 1)
        st = st.replace('11', '2', 1)
        st = st.replace('12', '21', 1)
        st = st.replace('010', '00', 1)
    sm=sum([int(x) for x in st])
    if sm>400 and f(sm):
        print(i)
        break

