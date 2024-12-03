def base4( n ):
  s = ''
  while n:
    s = str(n%4) + s
    n //= 4
  return s

count = 0
for i in range(4**3, 4**4):
  s = base4(i)
  if any( s.count(c) >= 2 for c in '0123' ) :
     count += 1

print( count )
