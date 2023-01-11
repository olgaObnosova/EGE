# coding: utf-8

insertAfter = 6

import sys

print ( 'Number of arguments:', len(sys.argv), 'arguments.' )
print ( 'Argument List:', str(sys.argv) )

def fileNumber ( fileName ):
  if fileName[-3:] != '.py': return -1
  num = fileName[:2]
  if not num.isdigit(): return -1
  return int(num)

def toBeChanged ( fileName ):
  return fileNumber(fileName) > insertAfter

mypath = "."
from os import listdir
from os.path import isfile, join
allFiles = [f for f in listdir(mypath)
              if isfile(join(mypath, f)) and toBeChanged(f) ]

print(allFiles)

import io
import os

sProg = "Программа № "
for fileName in allFiles:
  print(fileName)
  num = fileNumber(fileName) + 1
  with io.open(fileName,'r',encoding='utf8') as Fin:
    allStrings = Fin.readlines()
  wasChanged = False
  for i, s in enumerate(allStrings):
    p = s.find(sProg)
    p1 = s.find('.')
    if p >= 0 and p1 > p:
      s = s[:p+len(sProg)] + str(num) + s[p1:]
      allStrings[i] = s
      wasChanged = True
      break
  if wasChanged:
    num = str(num)
    if len(num) < 2: num = '0' + num
    os.remove(fileName)
    print("-" + fileName)
    fileName = num + fileName[2:]
    print("+" + fileName)
    with io.open(fileName,'w',encoding='utf8') as Fout:
      Fout.writelines(allStrings)
    # break

