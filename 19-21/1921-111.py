def next( x ): return x+10, x*2

TARGET = 82
def gameOver( x ): return x >= TARGET

def lose1( x ):
  return not gameOver(x) and all( gameOver(y) for y in next(x) )

def win1( x ):
  return not gameOver(x) and  any( lose1(y) for y in next(x) )

def lose2( x ):
  return all( gameOver(y) or win1(y) for y in next(x) ) and \
         any( win1(y) for y in next(x) )

def win2( x ):
  return any( lose2(y) for y in next(x) )

ans1, ans2, ans3 = [], [], []
for S in range(1, TARGET):
   if win1(S):  ans1.append(S)
   if lose2(S): ans2.append(S)
   if win2(S):  ans3.append(S)

print( f"1. {ans1}" )
print( f"2. {ans2}" )
print( f"3. {ans3}" )













