# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 16. Алфавитно-частотный словарь
#

wordList = {}
for s in open("input_16.txt"):
  word = s.strip() 	    # (1)
  if word:
    wordList[word] = wordList.get(word, 0) + 1

F = open("output_16.txt", "w")
for key in sorted( wordList ):
  F.write("{}: {}\n".format(key, wordList[key]))
F.close()


