a = 2 ** 100 + 2 ** 345 - 2 ** 12
s = ''
while a > 0:
    s += str(a % 3)

    a = a // 3
s = s[::-1]
print(s)


print(bin(90)[2:]) #2
print(oct(90)) #8
print(hex(90)) #16
print(int('12222',40))