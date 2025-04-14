import ipadress as ip
print(bin(46))
maxx=0
IPP=ip.ip_network('145.46.8.250/255.254.0.0', 0)
for x in IPP:
    t=bin(int(x)).count('1')
    if t>maxx:
        maxx=max(maxx, t)
        otv = x
print(maxx)
print(otv)
