f = open('24_25006979.txt')

st = ''

maxx = -100000
count = 1
for i in f:
    st += i
st=st.replace('XY','@')
st=st.replace('XZ','&')
for i in range(len(st)):
    if (st[i] != '@' and st[i] != '&'):
        count += 1
    else:
        maxx = max(count , maxx)
        count = 1
print(maxx+1)
