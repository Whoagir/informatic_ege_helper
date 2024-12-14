"""
######################################################################
  Программа для решения задачи 1921.64 (А. Кабанов)
  (C) К.Ю. Поляков, 2021
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""

TARGET = 45
KADD, KMUL = 2, 3
def gameOver( n1, n2 ):
  return n1+n2 >= TARGET

results = {}              # (1)
def gameResult( x, y ):
  if (x,y) in results: return results[(x,y)]     # (2)
  if gameOver(x, y): return 0
  nextCodes = [ gameResult( x+KADD, y ), gameResult( x*KMUL, y ),
                gameResult( x, y+KADD ), gameResult( x, y*KMUL ) ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[(x,y)] = res	# (3)
  return res

ans1 = []
ans2 = []
ans3 = []
for K in range(TARGET-1,0,-1):
  for S in range(TARGET-K-1,0,-1):
    r = gameResult( K, S )
    print( "(%d %d): %d" % (K, S, r) )
    if r == -1: ans1.append( (K, S) )
    if r == 2 and K == 4:
      ans2.append( (K, S) )
    if r == -2 and K == 13:
      ans3.append( (K, S) )

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", len(ans1), sorted(ans1) )
print("2. ", sorted(ans2))
print("3. ", ans3 )