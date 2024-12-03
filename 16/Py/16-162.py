
N = 23023
F = [2]*(N+1)
for i in range(2,N+1):
  F[i] = F[i-1] + i + 1

print( F[N] )