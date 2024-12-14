TARGET = 78
def gameOver( pos ):
  return pos[0] >= TARGET or pos[1] >= TARGET
def next( pos ):
  x, y = pos
  if x > y:
    return (x+1,y), (x+2,y), (x+3,y), (x,2*y),
  if x < y:
    return (x,y+1), (x,y+2), (x,y+3), (2*x,y),
  return (x+1,y), (x+2,y), (x+3,y), (x,y+1), (x,y+2), (x,y+3)

def win( pos, M ):
    if gameOver(pos): return M % 2 == 0
    if M == 0: return 0
    h = [ win( x, M-1 ) for x in next(pos) ]
    return any( h ) if M % 2 != 0 else \
           all( h )

allWin1 = [ (x,y) for x in range(1,TARGET) for y in range(1,TARGET)
                  if win( (x,y), 1 ) ]
print( '19)', sum( min( allWin1, key = sum ) ) )
print( '20)', [ pos[1] for pos in [(25,s) for s in range(1,TARGET)]
                    if win(pos, 3) and not win(pos, 1) ] )
print( '21)', [ pos[1] for pos in [(69,s) for s in range(1,TARGET)]
                    if win(pos, 4) and not win(pos, 2) ] )