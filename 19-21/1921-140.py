TARGET = 19
def gameOver( pos ):
  return pos <= TARGET
def next( pos ):
  return pos-2, pos-5, pos//3

def win( pos, M ):
    if gameOver(pos): return M % 2 == 0
    if M == 0: return 0
    h = [ win( x, M-1 ) for x in next(pos) ]
    return any( h ) if M % 2 != 0 else \
           all( h )

print( '19)', [ pos for pos in range(100, TARGET,-1) if win(pos, 2) ] )
print( '20)', [ pos for pos in range(100, TARGET,-1)
                    if win(pos, 3) and not win(pos, 1) ] )
print( '21)', [ pos for pos in range(100, TARGET,-1)
                    if win(pos, 4) and not win(pos, 2) ] )

