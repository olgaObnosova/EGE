import ipadress as ip
ad = ip.ip_network('190.202.83.62/255.255.252.0', 0)
for x in ad:
    print(x)
print(190+202+83+254)