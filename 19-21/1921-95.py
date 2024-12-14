"""
######################################################################
  Программа для решения задач 19-21 с одной кучей
  Статград: игрок не может делать такой же ход, как и его противник
  (C) К.Ю. Поляков, 2021
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
TARGET = 43
KADD1, KADD2, KMUL = 1, 2, 2
def gameOver( n1 ):
  return n1 >= TARGET

def nextVariants( x, previousMove ):
   nextCodes = [(gameResult( x+KADD1, 1 ), 1),
                (gameResult( x+KADD2, 2 ), 2),
                (gameResult( x*KMUL, 3 ), 3) ]
   return [ code for code in nextCodes
                 if code[1] != previousMove ]

results = {}              # (1)
def gameResult( x, previousMove = -1 ):
  print( x, previousMove )
  if (x, previousMove) in results:
    return results[(x, previousMove)]     # (2)
  if gameOver(x): return 0
  nextCodes = nextVariants( x, previousMove )
  negative = [c for c in nextCodes if c[0] <= 0]
  if negative:
    move = max( negative, key = lambda x: x[0] )
    res = - move[0] + 1
  else:
    move = max( nextCodes, key = lambda x: x[0] )
    res = - move[0]
  results[(x, previousMove)] = res	# (3)
  return res

from math import ceil
ans1 = ceil( TARGET/KMUL - 1 )
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