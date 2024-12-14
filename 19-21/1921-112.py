TARGET = 42
def next( x ):
  return (x+1, x+3, x+7) if x < TARGET else \
         (x-1, x-3, x-7)

def gameOver( x ): return x == TARGET

def win1( x ):
  return not gameOver(x) and any( gameOver(y) for y in next(x) )

def lose1( x ):
  return not gameOver(x) and all( win1(y) for y in next(x) )

def win2( x ):
  return not win1(x) and any( lose1(y) for y in next(x) )

def lose2( x ):
  return all( win1(y) or win2(y) for y in next(x) ) and \
         any( win1(y) for y in next(x) )

ans1 = TARGET - 7 - 7
ans2, ans3 = [], []
for S in range(1, 100):
   if win2(S):  ans2.append(S)
   if lose2(S): ans3.append(S)

print( f"1. {ans1}" )
print( f"2. {ans2}" )
print( f"3. {ans3}" )













