def f( n ):
  s = str(n % 2) + str(n % 2)
  while n:
    s = str(n%4) + s
    n //= 4
  s = s[-1] + s[:-1]
  return int(s,4)

max2dig = 0
for N in range(100):
  R = f(N)
  if 9 < R < 100:
    max2dig = max( R, max2dig )

print( max2dig )
