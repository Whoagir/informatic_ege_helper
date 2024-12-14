
def next( x, prevMoves ):
  nextMoves = [x+2, x+5, x+12, x*2]
  return [ (i, x) for i, x in enumerate(nextMoves)
                 if i != prevMoves[-2] ]

TARGET = 121
def gameOver( x ):
  return x >= TARGET

def win1( x, moves ):
  return x < TARGET and \
         any( gameOver(y) for i, y in next( x, moves ) )
def lose1( x, moves ):
  return all( win1(y, moves+[i])
              for i, y in next(x, moves) )
def win2( x, moves ):
  return any( lose1(y, moves+[i])
              for i, y in next(x, moves) )
def lose2( x, moves ):
  return any( win2(y, moves+[i])
              for i, y in next(x, moves) ) and \
     all( win2(y, moves+[i]) or
          win1(y, moves+[i])
          for i, y in next(x, moves) )
def win3( x, moves ):
  return any( lose2(y, moves+[i])
         for i, y in next(x, moves) ) and \
     not any( lose1(y, moves+[i])
         for i, y in next(x, moves) )
def lose3( x, moves ):
  return any( win3(y, moves+[i])
              for i, y in next(x, moves) ) and \
     all( win3(y, moves+[i]) or
          win2(y, moves+[i]) or
          win1(y, moves+[i]) for i, y in next(x, moves) )

from math import ceil
ans1 = ceil(TARGET/2/2)
ans2 = []
ans3 = []
for S in range(TARGET-1,0,-1):
  if win2(S, [-1, -1]): ans2.append(S)
  if lose3(S, [-1, -1]): ans3.append(S)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sorted(ans2))
print("3. ", sorted(ans3))