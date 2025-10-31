from re import *
with open('24_1975.txt') as f:
    f=f.readline()
reg = r'(?:[^P]|P(?!P))+' #имвол P, за которым не \
# следует P (отрицательный просмотр вперед).
sp=findall(reg, f)
st=max(sp, key=len)
print(len(st))