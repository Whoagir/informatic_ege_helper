
A = 7**500
for N in range(6,100):
  if (A - 5*N - 3) % 6 == 0:
    print( N )