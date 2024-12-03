x = 1
while True:
  n = 4*(x+2)
  print( x, n )
  if n >= 100000:
    print( x - 1)
    break
  x += 1