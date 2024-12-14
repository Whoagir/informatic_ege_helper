TARGET = 60
def gameOver( pos ):
  return sum(pos) >= TARGET
def next( pos ):
  x, y = pos
  if x == y:
    return (x+1,y), (x+2,y), (x+3,y), (x,y+1), (x,y+2), (x, y+3)
  elif x > y:
    return (x+1,y), (x+2,y), (x+3,y), (x,y*2)
  else:
    return (x*2,y), (x,y+1), (x,y+2), (x, y+3)

def win( pos, M ):
  if gameOver( pos ): return M % 2 == 0
  if M == 0: return 0
  h = [ win( x, M-1 ) for x in next(pos) ]
  return any( h ) if M % 2 != 0 else \
         all( h )

allWin1 = [ (x,y) for x in range(TARGET) for y in range(TARGET)
                if win( (x,y), 1 ) ]
print( '19)', sum( min( allWin1, key = sum ) ) )
print( '20)', [ pos[1] for pos in [(12,s) for s in range(1,47)]
                    if win(pos, 3) and not win(pos, 1) ] )
print( '21)', [ pos[1] for pos in [(25,s) for s in range(1,34)]
                    if win(pos, 4) and not win(pos, 2) ] )




