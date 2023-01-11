# -*- coding: utf-8
# Программа № 42. Игра с фишками (одностороннее домино)
def gameOver( start, fishSet ):
  if not start:
    return not fishSet
  final = start[-1]
  for fishka in fishSet:
    if final == fishka[0]:
      return False
  return True

def isWinPos( start, fishSet ):
  if gameOver( start, fishSet ):
    print( start )
    return False
  if start:
        final = start[-1]
  else: final = ""
  for fishka in fishSet:
    if final == ""  or final == fishka[0]:
      newSet = fishSet[:]
      newSet.remove(fishka)
      if not isWinPos( start+"-"+fishka, newSet ):
        return True
  return False
'''
def header():
  for i in range(10):
    print( "{:2} ".format(1+(i%2)), end="" )
  print()
  print('-'*30)
'''
fishSet = ["12", "14", "21", "22", "24", "41", "42", "44"]

start = "44"
fishSet.remove(start)
#fishSet.remove("22")

print( "Start: ", start )
#header()
if isWinPos( start, fishSet ):
  print( "Win!" )
else:
  print( "Lose..." )
