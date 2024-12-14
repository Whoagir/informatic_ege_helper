def gameOver( pos ):
  return pos >= 20
def lose0( pos ):
  return 20 <= pos <= 26
def win0( pos ):
  return pos > 26
def moves( pos ):
  return pos+4, 2*pos

def win1( pos ):
  return not gameOver(pos) and \
         any( lose0(move) for move in moves(pos) )

def lose1( pos ):
  return not gameOver(pos) and \
       all( win0(move) or win1(move) for move in moves(pos) )
"""
for S in range(19):
  if win1(S): print(S)
print('--------------------------------')
"""

for S in range(19):
  if lose1(S): print(S)

print('--------------------------------')

def win2( pos ):
  return not win1(pos) and \
         any( lose1(move) for move in moves(pos) )

for S in range(19):
  if win2(S): print(S)

print('--------------------------------')

def lose2( pos ):
  return all( win1(move) or win2(move)
              for move in moves(pos) ) and \
    any( win2(move) for move in moves(pos) )

for S in range(19):
  if lose2( S ): print(S)
