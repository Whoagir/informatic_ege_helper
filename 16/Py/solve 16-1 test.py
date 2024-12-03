from collections import Counter
from random import randint

def Ascending(n, reverse = False):
  n = str(n)
  if reverse: n = n[::-1]
  c0 = ' '
  for c in n:
    if c <= c0: return False
    c0 = c
  return True

memF = {}
def F(n, a, b, c):
  if n in memF: return memF[n]

  M = 15
  if n <= M: return a*n**2 + b*n + c

  if n % 3 == 0:
    val = F(n-1, a, b, c) + n - 2
  else:
    val = F(n-2, a, b, c) + n + 2

  memF[n] = val
  return val

def test( a, b, c ):
  count = 0
  s = []
  found = []
  for i in range(1,1000+1):
    #s.append( sum(map(int, str(F(i)))) )
    if Ascending(F(i, a, b, c)):
      found.append(F(i, a, b, c))
      count += 1
    #print(i, F(i))
  return count, found

best = 0
bestVal = 0
bestF = []
for i in range(10000):
  a = randint(1, 10)
  b = randint(1, 10)
  c = randint(1, 10)
  val, f = test(a, b, c)
  if val > bestVal:
    best = (a, b, c)
    bestVal = val
    bestF = f
    print( bestVal, (a, b, c), bestF )

#print(c)
#print(Counter(s))