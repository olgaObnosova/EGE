# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 34. Игра в тарелки. Разные скорости тарелок
#

import random
from graph import *

WIDTH = 500
HEIGHT = 600
MAX_PLATES = 10
MIN_R = 10
MAX_R = 30
MIN_V = 1
MAX_V = 5
COLORS = ["blue", "red", "yellow", "green"]
plates = []
vel = []

def init():
  windowSize( WIDTH, HEIGHT )
  canvasSize( WIDTH, HEIGHT )
  for i in range( MAX_PLATES ):
    r = random.randint( MIN_R, MAX_R )
    x = random.randint( r, WIDTH-r )
    y = random.randint( r, HEIGHT-r )
    v = random.randint( MIN_V, MAX_V )
    vel.append( v )
    color = random.choice( COLORS )
    brushColor( color )
    p = circle( x, y, r )
    plates.append( p )

def update():
  for i, p in enumerate(plates):
    moveObjectBy( p, -vel[i], 0 )
    x1, y1, x2, y2 = coords( p )
    if x2 <= 0:
      moveObjectBy( p, WIDTH+x2-x1, 0 )

init()
onTimer( update, 50 )

run()
