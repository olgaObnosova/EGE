# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 3 (10 класс)
# Программа № 33. Графы. Использование списков смежности
#

def pathCount ( graph, vStart, vEnd, visited ):
  if vStart == vEnd:
    print(visited + [vStart])
    return 1
  visited.append ( vStart )
  count = 0
  for v in graph[vStart]:
    if not v in visited:
      count += pathCount ( graph, v, vEnd, visited )
  visited.pop()
  return count

Graph = [ [3],
          [0, 2],
          [],
          [1, 2, 4],
          [2] ]
print ( pathCount(Graph, 0, 2, []) )
