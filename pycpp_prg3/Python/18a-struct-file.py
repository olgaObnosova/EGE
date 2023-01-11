# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 18a. Запись отдельных структур в файлы (Python 3.7+)
#

from dataclasses import dataclass

@dataclass
class TBook:
  author: str = "?"
  title: str = ""
  count: int = 0

import pickle

fileName = "books.dat"

# Запись по одной структуре
Fout = open( fileName, "wb")

b = TBook()

b.author = "Тургенев И.С."
b.title = "Муму"
b.count = 2
pickle.dump ( b, Fout );

b.author = "Васнецов И.С."
b.title = "Старуха"
b.count = 3
pickle.dump ( b, Fout );

Fout.close()

# Чтение в массив известного количества
Fin = open( fileName, "rb")
N = 2
books = [0]*N
for i in range(N):
  books[i] = pickle.load ( Fin )
Fin.close()

for b in books:
  print(b.author, b.title + ".", b.count, "шт.")

print()

# Чтение в массив неизвестного количества
Fin = open( fileName, "rb")
books = []
while True:
  try:
    books.append( pickle.load ( Fin ) )
  except:
    break
Fin.close()

for b in books:
  print(b.author, b.title + ".", b.count, "шт.")


