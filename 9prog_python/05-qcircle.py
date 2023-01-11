# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 5. Квадрокруг
#

from graph import *

def quadroCircle(xCenter, yCenter, R, level):
  if level < 1: return
  circle(xCenter, yCenter, R)
  nextR = R // 2
  quadroCircle( xCenter-R, yCenter, nextR, level-1 )
  quadroCircle( xCenter+R, yCenter, nextR, level-1 )
  quadroCircle( xCenter, yCenter-R, nextR, level-1 )
  quadroCircle( xCenter, yCenter+R, nextR, level-1 )

quadroCircle(200, 200, 100, 3)

run()