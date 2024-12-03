for x0 in range(1, 2):
 for s0 in range(1, 100):
  s, x = s0, x0
  #s = int(input())
  #x = int(input())
  s = 100*(s + x)
  n = 1
  while s < 2021:
    s = s + 5*n
    n = n + 1
  print( x0, s0, n )