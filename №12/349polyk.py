for n in range(100):
    st='7'+(n+2)*'2'+(n+1)*'1'+(n+3)*'3'
    while '71' in st or '72'in st or '73' in st:
        st=st.replace('71', '227', 1)
        st=st.replace('72', '37', 1)
        st = st.replace('73', '17', 1)
    if sum([int(x) for x in st])== n*9:
        print(n)
