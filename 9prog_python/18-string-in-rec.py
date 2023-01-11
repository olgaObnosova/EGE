# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 18. Рекурсивный перебор строк
#

def allWords(word, alphabet, K):
  if K < 1:
    print(word)
    return 1
  count = 0
  for c in alphabet:
    count += allWords( word+c, alphabet, K-1 )
  return count

alphabet = "АБВ"
K = 3
count = allWords( "", alphabet, K )
print( count )
