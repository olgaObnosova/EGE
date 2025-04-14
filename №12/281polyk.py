s=set()
for i in range(2, 10_000):
    st='5'*i
    while '555' in st or '888' in st:
        st=st.replace('555', '8', 1)
        st = st.replace('888', '55', 1)
    s.add(st)
print(len(s))