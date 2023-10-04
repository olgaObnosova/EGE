def pr(n):
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            return False
    return True
import ipaddress as p
cnt=0
for x in p.ip_network('172.118.0.0/255.255.252.0'):
    if pr(bin(int(x))[2:].count('1')):
        cnt+=1
print(cnt-1)# 1 широковещательный