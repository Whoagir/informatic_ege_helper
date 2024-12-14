"""
######################################################################
  Программа для решения задач 19-21 с двумя возможными ходами
  и одной кучей
  (C) К.Ю. Поляков, 2022
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""

TARGET = 10
KDIV, KSUB = 3, 10
def gameOver( n ):
  return n <= TARGET

results = {}              # (1)
def gameResult( x ):
  if x in results: return results[x]     # (2)
  if gameOver(x): return 0
  nextCodes = [ gameResult( x//KDIV ), gameResult( x-KSUB ), ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[x] = res	# (3)
  return res

ans1 = (TARGET+1)*KDIV**2 - 1
ans2 = []
ans3 = []
for S in range(10,200):
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
print("3. ", len(ans3), sorted(ans3))