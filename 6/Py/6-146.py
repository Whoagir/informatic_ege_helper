s1, s2 = 1, 0
x = 2
while True:
  s1 += 2*x
  s2 += x*(x-1)
  n = 3*s1 + s2
  print( x, s1, s2, n )
  if n > 1000000:
    print( x - 1)
    break
  x += 1