count = 0
for x in range(1, 100000):
  n = 1
  s = x
  while s > n:
    s = s - 15
    n = n * 5
  if n == 125:
    count += 1
    print( x, count )
