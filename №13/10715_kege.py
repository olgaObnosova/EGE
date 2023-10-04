import ipaddress as p
cnt=0
for x in p.ip_network('192.168.32.160/255.255.255.240'):
    if bin(int(x))[2:].count('0') > 21:
        cnt+=1
print(cnt)

