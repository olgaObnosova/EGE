import re
with open('24_25361.txt') as f:
    f=f.readline()
# reg = r'^[02468][^02468F]*F{76}$'
# comb = re.findall(reg, f)
# maxx=max(comb, key=len)
# print(maxx)
for x in '02468':
    f=f.replace(x, '*')
maxx=0
f=f.split('*') # [*a,aF,0aaaFaaFFaaaFFFFFa,*aFaaFa,*aaa,*a]
for x in f:
    st=''
    if x.count('F')>=76:
        for j in x:
            st+=j
            if st.count('F')==77:
                if len(st)-1 > maxx:
                    maxx = len(st)-1
                    otv = st
                    break
print(maxx+1)
print(otv)
# reg = r'^[02468](?=[13579A-Za-z]*$)(?=(?:[^Ff]*[Ff]){76}[^Ff]*$)[13579A-Za-z]*$'

