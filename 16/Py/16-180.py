from functools import cache
@cache
def F( n ): # сумма цифр троичной записи числа
  return n // 3 + n % 3 if n < 9 else \
         F(n//9) + F(n%9)

def tobase( n, b ):
  s = ''
  while n:
    s = str(n%b) + s
    n //= b
  return s

for i in range(10):
  print( i, F(i), tobase(i,3) )

print( '--------------------------' )
TARGET = 33
def F( s, L ):
  if L == 0: return int(s == TARGET)
  if s+2*L < TARGET: return 0
  return F( s, L-1 ) + F( s+1, L-1 ) + F( s+2, L-1 )

print( F( 0, 18 ) )
