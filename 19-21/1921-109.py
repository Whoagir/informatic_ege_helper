"""
######################################################################
  Программа для решения задач 19-21, аналогичных демо-варианту
  ЕГЭ по информатике 2021 года
  (C) К.Ю. Поляков, 2020
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-----------------------------------------------------------------
# Демо-вариант ФИПИ 2021 года
# Вариант с двумя возможными ходами
#-----------------------------------------------------------------

N1, TARGET = 17, 231
KADD, KMUL = 2, 2
def gameOver( n1, n2 ):
  return n1+n2 >= TARGET
def next( x, y):
  return ( x+KADD, y ), ( x*KMUL, y), \
         ( x, y+KADD ), ( x, y*KMUL )

results = {}              # (1)
def gameResult( x, y ):
  if (x,y) in results: return results[(x,y)]     # (2)
  if gameOver(x, y):
    results[(x,y)] = 0
    return 0
  nextCodes = [ gameResult(xn,yn) for xn, yn in next(x, y) ]
  negative = [c for c in nextCodes if c <= 0]
  if negative:
    res = -max(negative) + 1
  else:
    res = -max(nextCodes)
  results[(x,y)] = res	# (3)
  return res

def showTree( x, y, level = 0, whoWins = -1 ):
  r = results[(x,y)]
  if level == 0: whoWins = 0 if r > 0 else 1
  print( level*'  ', f"({x},{y}) -> {r}" )
  #if gameOver(x, y): return
  if level % 2 == whoWins % 2:
    for xi, yi in next(x, y):
      if -r < results[(xi,yi)] < 0: # только ход в проигрышную позицию
        showTree( xi, yi, level+1, whoWins )
        return
  else: # проверяем все ходы
    for xi, yi in next(x, y):
      showTree( xi, yi, level+1, whoWins )

from math import ceil
ans1 = (TARGET-1)-N1-KADD
ans2 = []
ans3 = []
for S in range(TARGET-N1-1,0,-1):
  r = gameResult( N1, S )
  print( "%d: %d" % (S, r) )
  if r == 2: ans2.append(S)
  if r == -2: ans3.append(S)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("1. ", ans1)
print("2. ", sorted(ans2))
print("3. ", sorted(ans3))

showTree( 17, 53 )
showTree( 17, 96 )