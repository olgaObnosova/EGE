#https://kompege.ru/variant?kim=25003645
f=open('24_25003645.txt')
st=f.readline()
st=st.replace('XYZ','@')
count=0
maxc=0
for i in range(len(st)):
    if st[i]=='@':
        count+=1
    else:
        maxc=max(maxc,count)
        count=0
print(maxc*3+1)# c ответом не согласна
