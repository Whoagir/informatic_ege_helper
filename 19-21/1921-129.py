TARGET = 14
def gameOver( pos ):
  x, y = pos
  return (pos[0]**2+pos[1]**2) >= TARGET**2
def next( pos ):
  x, y = pos
  return (2*x, y), (x, y+3), (x, y+4)

def win( pos, M ):
    if gameOver(pos): return M % 2 == 0
    if M == 0: return 0
    h = [ win( x, M-1 ) for x in next(pos) ]
    return any( h ) if M % 2 != 0 else \
           all( h )

print( '19)', [ pos for pos in range(1, TARGET) if win( (3, pos), 2) ] )
print( '20)', [ pos for pos in range(1, TARGET) if win( (3, pos), 3) ] )
print( '21)', [ pos for pos in range(1, TARGET)
                    if win( (3, pos), 4) and not win( (3, pos), 2) ] )

# Автор: А. Рогов

from functools import lru_cache
def move(x, y):
  return (2 * x, y), (x, y + 3), (x, y + 4)
@lru_cache(None)
def game(x, y):
  if (x ** 2 + y ** 2) ** 0.5 > e:
    return 5
  if any(game(a, b) == 5 for a, b in move(x, y)):
    return 1
  if all(game(a, b) == 1 for a, b in move(x, y)):
    return -1
  if any(game(a, b) == -1 for a, b in move(x, y)):
    return 2
  if all(game(a, b) > 0 for a, b in move(x, y)):
    return -2
  return 0

e = 14
for s in range(1, e):
 print(s, game(3, s))

