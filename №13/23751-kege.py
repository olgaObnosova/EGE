import ipaddress as t

adr = t.ip_network('191.128.66.83/255.192.0.0', 0)
for x in adr:
    ed = bin(int(x))[2:].count('1')
    k0= 32-ed

    print(x)