TARGET = 10
def gameOver( x ):
  return x <= TARGET
def moves( x ):
  return x-10, x//3

def win1( x ):
  return not gameOver(x) and \
         any( gameOver(y) for y in moves(x) )
def lose1( x ):
  return all( win1(y) for y in moves(x) )
def win2( x ):
  return not win1(x) and \
         any( lose1(y) for y in moves(x) )
def lose2( x ):
  return all( win1(y) or win2(y) for y in moves(x) ) and \
         any( win2(y) for y in moves(x) )

ans1 = (TARGET+1)*9 - 1
ans2 = [ x for x in range(11,200) if win2(x) ]
ans3 = [ x for x in range(11,200) if lose2(x) ]

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sorted(ans2))
print("3. ", len(ans3), sorted(ans3))