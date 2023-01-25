a = open('24-196.txt').readline()
a = a.replace('ZX','1').replace('ZY','1')
a = a.replace('Z',' ').replace('Y',' ').replace('X',' ')
print(max(map(len,a.split())))