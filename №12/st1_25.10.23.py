def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
minn=float('inf')
for i in range(1, 100):
    for j in range(1, 100):
        a='0'+i*'1'+j*'2'
        if len(a)>40:
            suma=a.count('1')+2*a.count('2')
            while '01' in a or '02' in a:
                a=a.replace('02', '1110',1)
                a=a.replace('01','220',1)
            s=a.count('1')+2*a.count('2')
            if pr(s) and len(a)>40:
                minn=min(minn,suma)

print(minn)