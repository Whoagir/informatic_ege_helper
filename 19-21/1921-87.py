"""
######################################################################
  Программа для решения задач 19-21 с тремя возможными ходами
  и тремя кучами (сводится к задаче с одной кучей)
  (C) К.Ю. Поляков, 2022
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
TARGET = 73
KADD, KADD2, KADD3 = 3, 13, 23
def gameOver( n ):
  return n >= TARGET

results = {}              # (1)
def gameResult( x ):
  if x in results: return results[x]     # (2)
  if gameOver(x): return 0
  nextCodes = [ gameResult( x+KADD ), gameResult( x+KADD2 ),
                gameResult( x+KADD3 ) ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[x] = res	# (3)
  return res

from math import ceil

ans1 = ceil((TARGET-2-2*max(KADD, KADD2, KADD3)) / 3)
ans2 = []
ans3 = []
for S in range(int((TARGET-2)/3),0,-1):
  s3 = 2 + S + 2*S
  r = gameResult( s3 )
  print( "%d: %d" % (S, r) )
  if r == 2: ans2.append(S)
  if r == -2:
    if 1 in [ gameResult( s3+KADD ), gameResult( s3+KADD2 ),
              gameResult( s3+KADD3 ) ]:
      ans3.append(S)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sorted(ans2))
print("3. ", sorted(ans3))