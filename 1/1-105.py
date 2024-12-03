from itertools import permutations

def coincide( A, B ):
  for r in range(len(A)):
    if A[r][:] != B[r][:]:
      return False
  return True

N = 7
W0 = [
[1, 0, 0, 1, 1, 0],
[0, 0, 0, 1, 1],
[1, 0, 0, 1],
[1, 0, 1],
[1, 1],
[1],
[],
]
W = []
for i, r0 in enumerate(W0):
  W.append( [0]*(i+1) + r0 )
for r in range(N):
  for c in range(r):
     W[r][c] = W[c][r]
#print( W )

letters = "АБВГДЕЖ"
L = [ "БВГ", "ГДЕ", "ГД", "Д", "ЕЖ", "Ж" ]
WW = [ [0]*N for i in range(N) ]
for i, Li in enumerate(L):
  for c in Li:
    t = letters.index(c)
    WW[i][t] = WW[t][i] = 1

#print( WW )

G = [ [0]*N for i in range(N) ]
for p in permutations(range(N)):
  for r in range(N):
    for c in range(N):
      G[r][c] = WW[p[r]][p[c]]
  if coincide(W, G):
    print(p)
    for x in p:
      print( letters[x], end="" )
    print()


