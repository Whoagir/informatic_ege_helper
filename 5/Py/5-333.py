def tri( n ):
  return str(n) if n < 3 else \
         tri(n // 3) + str(n%3)

Rmin = 10**10
for N in range(1, 1000):
  s = tri(N)
  if N % 3 == 0:
    s += s[-2:]
  else:
    s += tri( (N % 3)*5 )
  R = int(s, 3)
  if R > 133 and R < Rmin:
    print( N, R )
    Rmin = R
