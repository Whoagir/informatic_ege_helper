"""
######################################################################
  Программа для решения задач 19-21 с одной кучей
  Задача А. Богданова (уменньшение числа камней)
  (C) К.Ю. Поляков, 2021
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""

MAX = 37
TARGET = 1

def gameOver( n1 ):
  return n1 == TARGET

results = {}              # (1)
def gameResult( x ):
  if x in results: return results[x]     # (2)
  if gameOver(x):
    return 0
  nextCodes = []
  if x % 2 == 0:
    nextCodes.append( gameResult(x//2) )
  elif x > 2:
    nextCodes.append( gameResult(x-2) )
  if x % 3 == 0:
    nextCodes.append( gameResult(x//3) )
  elif x > 3:
    nextCodes.append( gameResult(x-3) )
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[x] = res	# (3)
  return res

from math import ceil
ans1 = []
ans2 = []
ans3 = []
for S in range(1, MAX+1):
  r = gameResult( S )
  print( "%d: %d" % (S, r) )
  if r == 1: ans1.append(S)
  if r == 2: ans2.append(S)
  if r == -2: ans3.append(S)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", max(ans1) )
print("2. ", sorted(ans2) )
print("3. ", sorted(ans3) )