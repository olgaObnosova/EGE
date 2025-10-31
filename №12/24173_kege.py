for i in range(1, 500):
    k1 = i #1
    k2 = k1 #2
    k0 = 1000-(k1+k2)
    st = k1*'1'+k2*'2'+k0*'0' #2221222
    smn = sum([int(x) for x in st])
    st = st.replace('0', '*')
    st = st.replace('1', '$')
    st = st.replace('2', '1')
    st = st.replace('$', '0')
    st = st.replace('*', '2')
    smk = sum([int(x) for x in st])
    if smn-smk==178:
        print(k1, k2, k0)
