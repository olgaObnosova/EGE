#https://kompege.ru/variant?kim=25003483
print(bin(45)[2:])
print(oct(45)+oct(56))
print(hex(45))
print(int('234a',16))

a=7*512**120-6*64**100+8**210-255
count=0
s=''
while a>0:
    
    s+=str(a%8)
        
    a=a//8

#print(s[::-1])
