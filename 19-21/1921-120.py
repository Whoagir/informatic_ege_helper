TARGET = 10
def gameOver( pos ):
  return pos[0] < TARGET or pos[1] < TARGET
def next( pos ):
  x, y = pos
  return (x-1,y), (x-3,y), (x,y-1), (x,y-3),

def win( pos, M ):
    if gameOver(pos): return M % 2 == 0
    if M == 0: return 0
    h = [ win( x, M-1 ) for x in next(pos) ]
    return any( h ) if M % 2 != 0 else \
           all( h )

print( '19)', [ pos[0] for pos in [(s,s) for s in range(TARGET+1, 2*TARGET)]
                       if win(pos, 2) ]  )
print( '20)', [ pos[1] for pos in [(13,s) for s in range(TARGET+1, 2*TARGET)]
                    if win(pos, 3) and not win(pos, 1) ] )
print( '21)', [ pos[1] for pos in [(13,s) for s in range(TARGET+1, 2*TARGET)]
                    if win(pos, 4) and not win(pos, 2) ] )

