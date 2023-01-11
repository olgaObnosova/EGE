s = '1234567890'
p = 0
for a in s:
    for b in s:
        for c in s:
            for d in s:
                for e in s:
                    for f in s:
                        word = (a + b + c + d + e + f)
                        if word[0] != '0' and word.count(
                        '13') == 0 and word.count('35') == 0 and word.count('57') == 0 and word.count(
                        '79') == 0 and (word[5] == '5' or '0' == word[5]) and word.count(
                        '31') == 0 and word.count('53') == 0 and word.count('75') == 0 and word.count(
                        '97') == 0 and word.count('1') == 1 and word.count('2') == 1  and word.count(
                        '3') == 1 and word.count('4') == 1  and word.count('5') == 1  and word.count(
                        '6') == 1 and word.count('7') == 1 and word.count('8') == 1 and word.count(
                        '9') == 1 and word.count('0') == 1:
                            p += 1

print(p)
