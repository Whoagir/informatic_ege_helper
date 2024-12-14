def gameOver( x, y ):
  return x == y

def next( x, y ):
  if x < y: return (x+1,y), (x+3,y)
  else:     return (x,y+1), (x,y+3)

def win1( x, y ):
  return any( gameOver(*moves) for moves in next(x, y) )

def lose1( x, y ):
  return all( win1(*moves) for moves in next(x, y) )

def win2( x, y ):
  return any( lose1(*moves) for moves in next(x, y) )

def lose1or2( x, y ):
  return all( win2(*moves) for moves in next(x, y) ) and \
         any( win1(*moves) for moves in next(x, y) ) and \
         not lose1(x, y)

results = []
for x in range(1, 23):
  if lose1(x, 13):
    results.append( x )
print( '19.', results )

results = []
for x in range(1, 23):
  if not win1(x, 13) and win2(x, 13):
    results.append( x )
print( '20.', results )

results = []
for x in range(1, 23):
  if lose1or2(x, 13):
    results.append( x )
print( '21.', results )

