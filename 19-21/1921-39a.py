"""
######################################################################
  Программа для решения задач 19-21 с двумя возможными ходами и одной кучей
  (C) К.Ю. Поляков, 2020
  Web:    http://kpolyakov.spb.ru
  e-mail: kpolyakov@mail.ru
######################################################################
"""
#-----------------------------------------------------------------
# Вариант с двумя возможными ходами и одной кучей
#-----------------------------------------------------------------

TARGET = 25
KADD, KMUL = 2, 2

def gameOver( n ):
  return n >= TARGET

def lose( n, byMove ):
  if gameOver(n): return True
  if byMove == 0: return False
  return win( n+KADD, byMove ) and \
         win( n*KMUL, byMove )

def win( n, byMove ):
  if gameOver(n): return False
  return lose( n+KADD, byMove-1 ) or \
         lose( n*KMUL, byMove-1 )

ans1, ans2, ans3 = [], [], []
for s in range(1,TARGET):
  if lose(s,1):
    ans1.append(s)
  if win(s,2) and not win(s,1):
    ans2.append(s)
  if lose(s,2) and not lose(s, 1):
    ans3.append(s)

#-------------------------------------------------------
# Ответы на вопросы
#-------------------------------------------------------
print("--- Ответы на вопросы ---")
print("19. ", ans1)
print("20. ", sorted(ans2))
print("21. ", ans3)