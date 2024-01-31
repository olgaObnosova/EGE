# for i in range(1203456009,10**12):
#     if i%98591==0:
#         print(i)
#         break
import  fnmatch as f
for i in range(1203500337, 10**12, 98591):
    if f.fnmatch(str(i),'12?3*456??9'):
        print(i,i//98591)
