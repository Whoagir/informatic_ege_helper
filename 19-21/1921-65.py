"""
######################################################################
  Программа для решения задачи 1921.65 (А. Кабанов)
  (C) К.Ю. Поляков, 2021
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""

TARGET = 18
KSUB, KDIV = 1, 2
def gameOver( n1, n2 ):
  return n1+n2 <= TARGET

results = {}              # (1)
def gameResult( x, y ):
  if (x,y) in results: return results[(x,y)]     # (2)
  if gameOver(x, y): return 0
  nextCodes = [ gameResult( x-KSUB, y ), gameResult( x, y-KSUB )]
  if x > 0: nextCodes.append( gameResult(x//KDIV, y) )
  if y > 0: nextCodes.append( gameResult(x, y//KDIV)  )
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
for K in range(3*TARGET, 0, -1):
  for S in range(3*TARGET, 0, -1):
    r = gameResult( K, S )
    print( "(%d %d): %d" % (K, S, r) )
    if r == -1 and K == S:
      ans1.append( (K, S) )
    if r == 2 and K == 13:
      ans2.append( (K, S) )
    if r == -2 and K == S:
      ans3.append( (K, S) )

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", len(ans1), ans1 )
print("2. ", sorted(ans2))
print("3. ", ans3 )