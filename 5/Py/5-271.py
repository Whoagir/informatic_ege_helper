def alg( x0, verbose = False ):
  x = x0
  s = ""
  while x:
    s = str(x%4) + s
    x //= 4
  if verbose: print ( x0, s )
  if x0 % 2 == 1:
    s = '2' + s + '11'
  else:
    s = '13' + s + '02'
  if verbose:
    print( s )
    print( int(s, 4) )
  return int(s, 4)

mi = 10**10
for x in range(100000):
  R = alg(x)
  if R > 1000:
    mi = min(mi, R)

print( mi )

alg( 45, True )