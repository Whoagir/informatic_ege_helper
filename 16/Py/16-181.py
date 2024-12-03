F = [0]*10011
for n in range(10010,49,-1):
  F[n] = 1 if n >= 10000 else \
         F[n+3] + 7 if n % 2 == 0 else \
         F[n+1] - 3

print( F[50] - F[57] )