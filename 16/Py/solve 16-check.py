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

  M = 13
  if n <= M: return n**3 + n**2 + 1

  if n % 3 == 0:
    val = F(n-1) + 2*n**2 - 3
  else:
    val = F(n-2) + 3*n + 6

  memF[n] = val
  return val

count = 0
s = []
found = []
for i in range(1,1000+1):
  s.append( sum(map(int, str(F(i)))) )
  if allEven(F(i)):
    found.append(F(i))
    count += 1

print(count)
print(found)
print(Counter(s))