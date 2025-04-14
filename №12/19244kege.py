for n in range(3, 10_001):
    st = '1' + n * '2'
    while '12' in st or '322' in st or '222' in st:
        if '12' in st:
            st = st.replace('12', '2', 1)
        if '322' in st:
            st = st.replace('322', '21', 1)
        if '222' in st:
            st = st.replace('222', '3', 1)
    s=0 # s=st.count('1')+2*st.count('2')+ 3*st.count('3')
    for x in st:
        s+=int(x)
    if s==15:
        print(n)
        break
