x = 1
while True:
  n = 2*(x*(x+1)-1) + x*(x-1)*x
  print( x, n )
  if n > 250000:
    print( x - 1)
    break
  x += 1