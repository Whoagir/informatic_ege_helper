def tri( n ):
  s = ''
  while n:
    s = str(n%3) + s
    n //= 3
  return s

for x in range(4100, 10000):
  n = 3 ** 100 - x
  s = tri( n )
  if s.count('0') == 1:
    print( x )
    break