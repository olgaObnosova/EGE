import ipadress as ip
adr = ip.ip_network('143.168.72.213/255.255.255.240', 0)
for x in adr:
    print(x)
print(bin(240))
print(bin(222))