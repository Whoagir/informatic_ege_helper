TARGET = 100
def gameOver( pos ):
  return pos >= TARGET
def next( pos ):
  return pos+7, pos*2

def win( pos, M ):
    if gameOver(pos): return M % 2 == 0
    if M == 0: return 0
    h = [ win( x, M-1 ) for x in next(pos) ]
    return any( h ) if M % 2 != 0 else \
           all( h )

print( '19)', TARGET - 1 - 7 )
print( '20)', [ pos for pos in range(1, TARGET) if win(pos, 2) ] )
print( '21)', [ pos for pos in range(1, TARGET)
                    if win(pos, 4) and not win(pos, 2) ] )

