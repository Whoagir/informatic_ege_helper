# Автор: Б. Баобаба

A = 'AEGIKOPRSTUV'

def f( n ):
  a = [-1]*(n + 1)
  a[0] = 1
  a[1] = 0
  for i in range(2, n+1):
    a[i] = (i-1)*(a[i-1] + a[i-2])
  return a[n]

print( f(len(A)) )

#----------------------------------------
# Очень долго считает, но можно даждаться...

from itertools import permutations

n = 0
for w in permutations(A):
  if all( w.index(c) != A.index(c) for c in A ):
    n += 1

print( n )
