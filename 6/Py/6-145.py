s1, s2 = 3, 1
x = 2
while True:
  s1 += 4
  s2 += x
  n = 4*s1 + 2*s2
  print( x, s1, s2, n )
  if n > 5500000:
    print( x - 1)
    break
  x += 1
