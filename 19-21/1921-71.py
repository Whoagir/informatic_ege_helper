"""
######################################################################
  Программа для решения задач 19-21, аналогичных демо-варианту
  ЕГЭ по информатике 2021 года
  (C) К.Ю. Поляков, 2020
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-----------------------------------------------------------------
# Вариант с двумя возможными ходами
#-----------------------------------------------------------------

N1, TARGET = 8, 68
KADD = 1
def gameOver( n1, n2 ):
  return n1+n2 >= TARGET

results = {}              # (1)
def gameResult( x, y ):
  if (x,y) in results: return results[(x,y)]     # (2)
  if gameOver(x, y): return 0
  nextCodes = [ gameResult( x+KADD, y ), gameResult( x+y, y ),
                gameResult( x, y+KADD ), gameResult( x, y+x ) ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[(x,y)] = res	# (3)
  return res

from math import ceil
ans1 = ceil((TARGET-2*N1)/3)
ans2 = []
ans3 = []
for S in range(TARGET-N1-1,0,-1):
  r = gameResult( N1, S )
  print( "%d: %d" % (S, r) )
  if r == 2: ans2.append(S)
  if r == -2: ans3.append(S)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sorted(ans2))
print("3. ", ans3)