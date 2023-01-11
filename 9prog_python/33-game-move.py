# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 33. Игра в тарелки. Движение
#

import random
from graph import *

WIDTH = 500
HEIGHT = 600
MAX_PLATES = 10
MIN_R = 10
MAX_R = 30
COLORS = ["blue", "red", "yellow", "green"]
plates = []

def init():
  windowSize( WIDTH, HEIGHT )
  canvasSize( WIDTH, HEIGHT )
  for i in range( MAX_PLATES ):
    r = random.randint( MIN_R, MAX_R )
    x = random.randint( r, WIDTH-r )
    y = random.randint( r, HEIGHT-r )
    color = random.choice( COLORS )
    brushColor( color )
    p = circle( x, y, r )
    plates.append( p )

def update():
  for p in plates:
    moveObjectBy(p, -5, 0)
    x1, y1, x2, y2 = coords( p )
    if x2 < 0:
      moveObjectBy( p, WIDTH+x2-x1, 0 )

init()
onTimer( update, 50 )

run()
