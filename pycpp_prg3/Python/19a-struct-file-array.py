# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 19a. Запись массива структур в файлы (Python 3.7+)
#

from dataclasses import dataclass

@dataclass
class TBook:
  author: str = "?"
  title: str = ""
  count: int = 0

import pickle

fileName = "books_arr.dat"

# Запись массива в файл
Fout = open( fileName, "wb")

N = 2
books = [TBook() for i in range(N)]

books[0].author = "Тургенев И.С."
books[0].title = "Муму"
books[0].count = 2

books[1].author = "Васнецов И.С."
books[1].title = "Старуха"
books[1].count = 3

pickle.dump ( books, Fout );

Fout.close()

# Чтение массива из файла

Fin = open( fileName, "rb")
books = pickle.load ( Fin )
Fin.close()

for b in books:
  print(b.author, b.title + ".", b.count, "шт.")
print()



