"""
######################################################################
  Программа для решения задач 19-21 с тремя кучами камней
  (C) К.Ю. Поляков, 2021
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
N1, N2, TARGET = 7, 5, 71
KADD, KMUL = 3, 2
def gameOver( n1, n2, n3 ):
  return n1+n2+n3 >= TARGET

results = {}              # (1)
def gameResult( x, y, z ):
  if (x,y,z) in results: return results[(x,y,z)]     # (2)
  if gameOver(x, y, z): return 0
  nextCodes = [ gameResult( x+KADD, y, z ), gameResult( x*KMUL, y, z ),
                gameResult( x, y+KADD, z ), gameResult( x, y*KMUL, z ),
                gameResult( x, y, z+KADD ), gameResult( x, y, z*KMUL ) ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[(x,y,z)] = res	# (3)
  return res

from math import ceil
ans1 = min( ceil((TARGET-N1-N2)/KMUL/KMUL),
            ceil(TARGET-N1-N2*KMUL*KMUL), ceil(TARGET-N2-N1*KMUL*KMUL) )
ans2 = []
ans3 = []
for S in range(TARGET-N1-N2-1,0,-1):
  r = gameResult( N1, N2, S )
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