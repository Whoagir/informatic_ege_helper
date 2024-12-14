TARGET = 121
def next( x, moves ):
  nextMoves = [x+2, x+5, x+12, x*2]
  return [ (i, y) for i, y in enumerate(nextMoves)
                  if i != moves[-2] ]

def gameOver( n ):
  return n >= TARGET

results = {}
def gameResult( x, moves ):
  if (x,moves) in results: return results[(x,moves)]
  if gameOver(x): return 0
  nextCodes = [ gameResult( n, tuple(list(moves)+[i]) )
                for i, n in next(x, moves) ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[(x,moves)] = res	# (3)
  return res

from math import ceil
ans1 = ceil(TARGET/2/2)
ans2 = []
ans3 = []
for S in range(TARGET-1,31,-1):
  r = gameResult( S, (-1, -1) )
  print( "%d: %d" % (S, r) )
  if r == 2: ans2.append(S)
  if r == -3: ans3.append(S)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sorted(ans2))
print("3. ", sorted(ans3))