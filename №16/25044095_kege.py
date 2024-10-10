sp=[0]*8000
for i in range(7999, -1,-1):
    if i>=7777:
        sp[i]=i
    else:
        sp[i]=i+5+sp[i+5]
print(sp[1101]-sp[1111])