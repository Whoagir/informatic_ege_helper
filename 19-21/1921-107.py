TARGET = 178

def gameOver( n ):
  return sum(n) >= TARGET

def moves( xy ):
  x, y = xy
  return (x+4,y), (x,y+3), (2*x,y), (x,3*y)

def win1( xy ):
  return not gameOver(xy) and \
         any( gameOver(m) for m in moves(xy) )

def lose1( xy ):
  return all( win1(m) for m in moves(xy) )

def win2( xy ):
  return not win1(xy) and \
         any( lose1(m) for m in moves(xy) )

def lose2( xy ):
  return all( win1(m) or win2(m) for m in moves(xy) ) and \
         any( win2(m) for m in moves(xy) )

def win3( xy ):
  return not win2(xy) and \
         any( lose2(m) for m in moves(xy) )

from math import ceil
N = 21
ans1 = min( ceil( (TARGET - N)/9 ),
            TARGET - N*2*2,
            ceil( (TARGET - N*2)/3 )
             )
ans2 = [ y for y in range(1,157) if win2( (N,y) ) ]
ans3 = [ y for y in range(1,157) if win3( (N,y) ) ]

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sum(ans2))

from functools import reduce
print("3. ", reduce(lambda x, y: x*y, ans3))