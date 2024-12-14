TARGET = 166
def gameOver( x ):
  return x >= TARGET
def next( x ):
  moves = [x+2, x+10]
  k = 2
  while k*x-x <= 80:
    moves.append( k*x )
    k += 1
  return moves

def win( pos, M ):
    if gameOver(pos): return M % 2 == 0
    if M == 0: return 0
    h = [ win( x, M-1 ) for x in next(pos) ]
    return any( h ) if M % 2 != 0 else \
           all( h )

print( '19)', 1  )
print( '20)', [ x for x in range(1, TARGET)
                  if win(x, 3) and not win(x, 1) ] )
print( '21)', [ x for x in range(1,TARGET)
                  if win(x, 4) and not win(x, 2) ] )
