# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 23. Ввод массива
#

N = 5
A = [0]*N
print("Введите 5 элементов массива")
for i in range(N):
  A[i] = int(input())

print(A)

print("Введите 5 элементов массива")
A = [ int(input()) for i in range(N) ]
print(A)

print("Введите 5 элементов массива")
for i in range(N):
  print( "A[{}]=".format(i), end="" )
  A[i] = int(input())
print(A)
