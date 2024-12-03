G = "АБГЗ БАВ ВБД ГАЗ ДВЖ ЖДЗ ЗАГЖ"
G = { s[0]: ''.join(sorted(s[1:])) for s in G.split() }

D = [
[],
[16],
[0, 22],
[0, 0, 0],
[0, 0, 11, 14],
[0, 0, 0, 21, 0],
[8, 18, 0, 0, 0, 13]
]

N = len(G)
W = [ [0]*N for _ in range(N) ]
for i in range(N):
  for j, x in enumerate(D[i]):
    W[i][j] = W[j][i] = D[i][j]

from itertools import permutations

for p in permutations(G):
  #print(p)
  G1 = {}
  for i, v in enumerate(p):
    G1[v] = ''.join( sorted( p[j] for j in range(N) if W[i][j] > 0 ) )
  if G == G1:
    print( { v: i+1  for i, v in enumerate(p) } )
    print( G1 )
    print()
