"""
######################################################################
  Программа для решения задачи 1921.52 (Е. Джобс)
  (C) К.Ю. Поляков, 2021
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-----------------------------------------------------------------
# Вариант с двумя возможными ходами и одной кучей
#-----------------------------------------------------------------

TARGET = 1000
KADD, KMUL = 100, 2
def gameOver( n ):
  return n >= TARGET

results = {}              # (1)
def gameResult( x ):
  if x in results: return results[x]     # (2)
  if gameOver(x): return 0
  nextCodes = [ gameResult( x+KADD ), gameResult( x*KMUL ) ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[x] = res	# (3)
  return res

def hasMove( fromS, toResult ):
  return toResult in \
         [gameResult(fromS+KADD), gameResult(fromS*KMUL)]

ans1 = []
ans2 = []
ans3 = []
for S in range(TARGET-1,0,-1):
  r = gameResult( S )
  print( "%d: %d" % (S, r) )
  if r == -1: ans1.append(S)
  if r == 2: ans2.append(S)
  if r == -2 and hasMove(S, 1):
    ans3.append(S)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", len(ans1), sorted(ans1))
print("2. ", len(ans2), sorted(ans2))
print("3. ", len(ans3), sorted(ans3))