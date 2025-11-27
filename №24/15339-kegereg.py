from re import  *
with open('24_15339.txt') as f:
    f=f.readline()
reg = r'(?:[ABC][6789])+(?:[ABC])?|'+ r'(?:[6789][ABC])+(?:[6789])?'
sp = findall(reg, f)
str= max(sp, key=len)
print(len(str))