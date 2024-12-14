"""
######################################################################
  Программа для решения задач 19-21 с одной кучей
  (C) К.Ю. Поляков, 2021
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
TARGET, FAIL = 50, 70
KADD, KMUL = 1, 2
def gameOver( n1 ):
  return n1 >= TARGET

results = {}              # (1)
def gameResult( x ):
  if x in results: return results[x]     # (2)
  if gameOver(x):
    return 0 if x <= FAIL else 1
  nextCodes = [ gameResult( x+KADD ), gameResult( x*KMUL ) ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[x] = res	# (3)
  return res

from math import ceil
ans1 = ceil(TARGET/KMUL/KMUL)
ans2 = []
ans3 = []
for S in range(TARGET-1,0,-1):
  r = gameResult( S )
  print( "%d: %d" % (S, r) )
  if r == 2: ans2.append(S)
  if r == -2: ans3.append(S)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sorted(ans2))
print("3. ", sorted(ans3))