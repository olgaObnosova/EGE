# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 8. Простая работа с файлами
#

Fin = open("input_8.txt")
s = Fin.readline().split()
a, b = [int(x) for x in s]
# a, b = map( int, s )
Fin.close()

Fout = open("output_8.txt", "w")
Fout.write( "{}+{}={}\n".format(a,b,a+b) )
Fout.close()

