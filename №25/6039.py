import fnmatch as f
for i in range(1058129, 10**8):
    if f.fnmatch(str(i),'1?58*129'):
        if (i%117==0 and i%119!=0 and i%121!=0) or \
                (i % 117 != 0 and i % 119 == 0 and i % 121 != 0) or \
                (i % 117 != 0 and i % 119 != 0 and i % 121 == 0):
            print (i,i%117,i//117, i%119,i//119,i%121, i//121)