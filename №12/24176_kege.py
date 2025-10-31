for i in range(1, 500):
    k0=i #0
    k1 =k0 #1
    k2=1000-(k1+k0) #2
    st = k1*'1'+k2*'2'+k0*'0' #2221222
    smn = sum([int(x) for x in st]) # st.count('1)+st.count('2')*2
    st=st.replace('0', '*')
    st = st.replace('1', '$')
    st = st.replace('2', '2')
    st = st.replace('$', '0') # 0 -
    st = st.replace('*', '')
    smk = sum([int(x) for x in st])
    if smn-smk==363:
        print(k1, k2, k0, st.count('0'))
