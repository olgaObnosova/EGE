# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 17. Структуры
#

#class TBook:
#  pass

class TBook:
  author = "?"
  title = ""
  count = 0

b = TBook()
b.author = "Пушкин А.С."
b.title = "Полтава"
b.count = 1

fam = b.author.split()[0]	# только фамилия
print( fam )
b.count -= 1        		# одну книгу взяли
if b.count == 0:
  print("Этих книг больше нет!")
print( b.author, b.title + ".", b.count, "шт." )

# books = [TBook()]*100  # это ошибка!
books = []
for i in range(100):
  books.append( TBook() )

N = 100
books = [ TBook() for i in range(N) ]
