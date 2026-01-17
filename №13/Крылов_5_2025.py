import ipadress as ip
A = ip.ip_network('204.16.168.0/255.255.248.0', 0)
k=0
for x in A:
    x=bin(int(x))[2:]
    if x.count('1')%5!=0:
        k+=1
print(k)