with open('26-106.txt') as F:
  N, M, K = map(int, F.readline().split())
  D = [ [1]*M for i in range(N) ]
  for i in range(K):
    r, p = map(int, F.readline().split())
    r, p = r-1, p-1
    D[r][p] = 0
    if p > 0: D[r][p-1] = 0
    if p < M-1: D[r][p+1] = 0

D = [ (sum(row), i+1) for i, row in enumerate(D) ]
D.sort( key = lambda x: (-x[0], x[1] ))

print( sum( x[0] for x in D ),
       D[0][1])
