with open('st_17.12.2024') as f:
    sp=[[int(x) for x in line.split()] for line in f]
st1=[0]*101
st2=[0]*101
st3=[0]*101
st4=[0]*101
st5=[0]*101
st6=[0]*101
for x in sp:
    st1[x[0]]+=1
    st2[x[1]] += 1
    st3[x[2]]+=1
    st4[x[3]] += 1
    st5[x[4]] += 1
    st6[x[5]] += 1
cnt=0
for x in sp:
    k=k1=0
    if st1[x[0]] >= 330 and x[0] not in x:
        k += 1
    if st2[x[1]] >= 330 and x[1] not in x:
        k += 1
    if st3[x[2]] >= 330 and x[2] not in x:
        k += 1
    if st4[x[3]] >= 330 and x[3] not in x:
        k += 1
    if st5[x[4]] >= 330 and x[4] not in x:
        k += 1
    if st6[x[5]] >= 330 and x[5] not in x:
        k += 1
    if x[0] > sum(x) / len(x):
        k1 += 1
    if x[1] > sum(x) / len(x):
        k1 += 1
    if x[2] > sum(x) / len(x):
        k1 += 1
    if x[3] > sum(x) / len(x):
        k1 += 1
    if x[4] > sum(x) / len(x):
        k1 += 1
    if x[5] > sum(x) / len(x):
        k1 += 1
    if k == 1 and k1 == 1:
        cnt += 1
print(cnt)

