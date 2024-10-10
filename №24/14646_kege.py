with open("C:\\Users\\oppoe\\Downloads\\24.3_14646.txt") as f:
    s = f.readline()
alf_sg = ['B', 'C', 'D',  'F', 'G', 'H',  'J', 'K', 'L', 'M', 'N',  'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
alf_gl = ['A','E', 'I','O','U', 'Y',]
for i in range(len(alf_sg)):
    s = s.replace(alf_sg[i], '1')
for i in range(len(alf_gl)):
    s = s.replace(alf_gl[i], '2')
print(s)