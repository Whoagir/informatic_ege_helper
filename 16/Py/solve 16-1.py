from collections import Counter
from random import randint

even = '02468'
odd = '13579'

def allEven(n):
  n = str(n)
  for c in n:
    if c not in even: return False
  return True
def allOdd(n):
  n = str(n)
  for c in n:
    if c not in odd: return False
  return True

memF = {}
def F(n):
  if n in memF: return memF[n]

  M = 3
  if n <= M: return n

  if n % 2 == 0:
    val = 2*n + F(n-1)
  else:
    val = n*n + F(n-2)

  memF[n] = val
  return val

count = 0
s = []
found = []
for i in range(1,100+1):
  s.append( sum(map(int, str(F(i)))) )
  if F(i) % 3 == 0:
    found.append(F(i))
    count += 1
  print(i, F(i))

print(count)
print(found)
print(Counter(s))