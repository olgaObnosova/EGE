# def f (A):
#     for x in range(1, 1000):
#             if ((x%A!=0) <=((x%28==0)<=(x%49!=0))) == False:
#                 return False
#     return True
# for A in range (1,1000):
#      if f(A):
#           print (A)
def f (x,A):
    return (x%A!=0) <= ((x%28==0) <= (x%49!=0))

for A in range (1,1000):
     if all(f(x,A)==1 for x in range(1,1000)):
          print (A)