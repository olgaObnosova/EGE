from ipaddress import *

net = ip_network('111.222.0.124/255.255.224.0', 0)
k=0
for ip in net:
	k1= bin(int(ip)).count('1')
	k0 = 32-k1
	if (k1*k0)%2!=0:
		print(ip)
print(111+222+31+255)