# -*- coding: utf-8
#
# Программа к учебному пособию
# К.Ю. Поляков. Программирование на языках Python и C++
# Часть 2 (9 класс)
# Программа № 17. Символьные строки в функциях
#

def extractFileName( fileAddr ):
  fileAddr = fileAddr.replace("\\", "/")
  posSlash = fileAddr.rfind("/")
  fileName = fileAddr[posSlash+1:]
  return fileName

address = "/home/vasya/miner.exe"
fName = extractFileName( address )
print( fName )

address = "c:\doc\vasya\miner.exe"
fName = extractFileName( address )
print( fName )


