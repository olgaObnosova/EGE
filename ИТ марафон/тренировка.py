with open('m9-1.txt') as f:
    f=f.readline().split('BB')
maxx=0
minn=10**10
print(len(f))# количество строк
for x in f:
    if len(x)>maxx: # самая большая
        maxx=len(x)
    if len(x)<minn: #самая маленькая
        minn=len(x)
    if len(x)>0:
        print(x[0]) # каждый 1-й
print(maxx)
print(minn)