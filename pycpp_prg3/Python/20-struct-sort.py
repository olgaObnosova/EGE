# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 20. Сортировка массива структур
#

import pickle

fileName = "books_arr.dat"

class TBook:
  pass

# Чтение массива из файла
Fin = open( fileName, "rb")
books = pickle.load ( Fin )
Fin.close()

for b in books:
  print(b.author, b.title + ".", b.count, "шт.")
print()

# Сортировка массива структур
N = len(books)
for i in range(0,N-1):
  for j in range(N-2,i-1,-1):
    if books[j].author > books[j+1].author:
      books[j],books[j+1] = books[j+1],books[j]

for b in books:
  print(b.author, b.title + ".", b.count, "шт.")
print()

# Сортировка массива структур встроенными средствами
def getAuthor( b ):
  return b.author
books.sort( key = getAuthor )
for b in books:
  print(b.author, b.title + ".", b.count, "шт.")
print()

books.sort( key = lambda x: x.author, reverse=True )
for b in books:
  print(b.author, b.title + ".", b.count, "шт.")
print()

for b in sorted( books,
                 key = lambda x: x.author ):
  print(b.author, b.title + ".", b.count, "шт.")


