file = open("2518")
kor_191 = 0
kor_103 = 0
for line in file:
    stroka = [int(i.strip("\n")) for i in line.split("\t")]
    dlina = 0.01 * stroka[0]
    shirina = 0.01 * stroka[1]
    height= 0.01 * stroka[2]
    s = dlina * height *2 + shirina * height *2 + dlina * shirina * 2
    if s < 10.0:
        kor_191 += 1
    else:
        kor_103 +=1
sneg_191 = 0
sneg_103 = 0
print(kor_103)
print(kor_191)
if kor_191 % 191 > 0:
    sneg_191 = 1
if kor_103 % 103 > 0:
    sneg_103 =1
snegoviki = kor_191 // 191 + sneg_191 + sneg_103 + kor_103 // 103
print(snegoviki)