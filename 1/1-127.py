letters = "АБВГДЕЖЗ"
#      А      Б    В    Г     Д     Е    Ж
L = [ "ВЕ", "ГЖ", "Д", "Д", "ЕЖЗ", "З", "З" ]
N = len(letters)
W0 = [
[0, 14, 0, 0, 18, 0, 0],
[0, 15, 22, 0, 0, 0],
[0, 0, 0, 15, 17],
[0, 0, 20, 15],
[0, 15, 0],
[19, 0],
[25],
[],
]


from itertools import permutations

def coincide( A, B ):
  for r in range(len(A)):
    for c in range(r+1, len(A[r])):
      if( A[r][c] == 0 and B[r][c] != 0 or
          A[r][c] != 0 and B[r][c] == 0 ): return False
  return True

W = []
for i, r0 in enumerate(W0):
  W.append( [0]*(i+1) + r0 )
for r in range(N):
  for c in range(r):
     W[r][c] = W[c][r]

# print( W )

WW = [ [0]*N for i in range(N) ]
for i, Li in enumerate(L):
  for c in Li:
    t = letters.index(c)
    WW[i][t] = WW[t][i] = 1

# print( WW )

def printMatrix( W, p ):
  print('\n   ', end='')
  for i in p:
    print( f"{letters[i]:3}", end='')
  print()
  for i in range(N):
    print( f"{letters[p[i]]}", end='')
    for j in range(N):
      print( f"{W[i][j]:3}", end='' )
    print()


G = [ [0]*N for i in range(N) ]
for p in permutations(range(N)):
  for r in range(N):
    for c in range(N):
      G[r][c] = WW[p[r]][p[c]]
  if coincide(W, G):
    print(p)
    for x in p:
      print( letters[x], end="" )
    printMatrix( W, p )
    print()


