N = 200024
F = [0]*(N+1)
F[1] = F[2] = 1
for i in range(3,N+1):
  F[i] = 3*F[i-2] + F[i-1]

print( F[N] // F[N-4] )