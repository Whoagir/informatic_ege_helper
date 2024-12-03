
N = 23023
F = [5]*(N+1)
for i in range(3,N+1):
  F[i] = F[i-2] + i

print( F[N] )