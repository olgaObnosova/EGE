import ipadress as ip
adr = ip.ip_network('191.128.66.83/255.192.0.0', 0)
for x in adr:
    print(x)

