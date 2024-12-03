from itertools import permutations

def coincideMask( A, B ):
  for r in range(len(A)):
    for c in range(r+1, len(A[r])):
      if( A[r][c] == 0 and B[r][c] != 0 or
          A[r][c] != 0 and B[r][c] == 0 ): return False
  return True

N = 7
W0 = [
[8, 11, 0, 13, 0, 0],
[12, 15, 0, 0, 14],
[0, 10, 0, 0],
[0, 0, 16],
[18, 22],
[17],
[],
]
W = []
for i, r0 in enumerate(W0):
  W.append( [0]*(i+1) + r0 )
for r in range(N):
  for c in range(r):
     W[r][c] = W[c][r]
print( W )

letters = "АБВГДЕЖ"
L = [ "БВГ", "ВЕЖ", "Г", "ДЕ", "Е", "Ж" ]
WW = [ [0]*N for i in range(N) ]
for i, Li in enumerate(L):
  for c in Li:
    t = letters.index(c)
    WW[i][t] = WW[t][i] = 1

print( WW )

G = [ [0]*N for i in range(N) ]
for p in permutations(range(N)):
  for r in range(N):
    for c in range(N):
      G[r][c] = WW[p[r]][p[c]]
  if coincideMask(W, G):
    print(p)
    for x in p:
      print( letters[x], end="" )
    print()


