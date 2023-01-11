'''
for i in range(1049341,999999999):
    if i%2023==0:
        print(i)
        break
'''
for i in range(1049937,10000000000,2023):
    a=str(i)
    if a[0]=='1' and a[2:5]=='493' and a[-2]=='4' and a[-1]=='1':
        print(i, i%2023)
