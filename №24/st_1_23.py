gl='AO'
sogl='CDF'
k=0
maxk=0
f=open('24st_1_23.txt').readline()
j=0
for i in range(len(f)-2):
    if f[j] in sogl and f[j+1] in sogl and f[j+2] in gl:
        k+=1
        j+=3
    else:
        j=i
        maxk=max(maxk,k)
        k=0
print(maxk)     
