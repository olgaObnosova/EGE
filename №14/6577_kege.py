a=673**7+67**6+3**3
sa=0
s8=0
while a!=0:
    if a%12==10:
        sa=sa+a%12
    if a%12==8:
        s8+=a%12
    a=a//12
print(sa-s8)
