# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 43. Время на выполнение операций
#

# Количество операций
def T(N):
  return (N*N-N)/2

operPerSecond = 1e6
N = 1000
for i in range(5):
  t = T(N) / operPerSecond
  print("{:9}: {:10.3f} sec  {:10.3f} min  {:10.3f} hours  {:10.3f} days".format(
            N, t, t/60, t/3600, t/3600/24))
  N *= 10