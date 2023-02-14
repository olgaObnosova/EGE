minn=float('inf')
for i in range(100,1,-1):
    a='0'+i*'2'+i*'1'+i*'2'+i*'1'+'0'
    while '00' not in a:
        if '01' in a:
            a=a.replace('011','101',1)
        else:
            a = a.replace('01', '40', 1)
            a = a.replace('02', '20', 1)
            a = a.replace('0222', '1401', 1)
    print(a)
    if a.count('0')==9 and a.count('1')==6:
        minn=min(minn,a.count('4'))
print(minn)