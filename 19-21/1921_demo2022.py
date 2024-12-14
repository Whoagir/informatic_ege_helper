TARGET = 29
def gameResult( S ):
  if S >= TARGET: return 0
     # рекурсивно определяем коды всех возможных ходов
  nextCodes = [ gameResult(S+1), gameResult(S*2) ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  return res

results = [(S,gameResult(S)) for S in range(1,TARGET)]
print( '19:', [S for S, R in results if R == -1] )
print( '20:', [S for S, R in results if R == 2] )
print( '21:', [S for S, R in results if R == -2] )
