def tri( n ):
  return str(n) if n < 3 else \
         tri(n // 3) + str(n%3)

for N in range(1, 1000):
  s = tri(N)
  if N % 3 == 0:
    s = '1' + s + '02'
  else:
    s += tri( (N % 3)*4 )
  R = int(s, 3)
  if R < 199:
    print( N, R )
