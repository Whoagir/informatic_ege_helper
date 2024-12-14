from functools import lru_cache
TARGET = 20
@lru_cache
def gameResult( S, superMove = False ):
  if S >= TARGET: return 0
  # рекурсивно определяем коды всех возможных ходов
  nextCodes = [ gameResult(S+2, superMove), gameResult(S*2, superMove) ]
  if not superMove:
    nextCodes.append( gameResult(S, True) )
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  return res

from math import ceil
results = [(S,gameResult(S)) for S in range(1,TARGET)]
print( '19:', ceil(TARGET/2/2) )
print( '20:', [S for S, R in results if R == 2] )
print( '21:', [S for S, R in results if R < 0] )
# print(results)