def f(x, y, A):
  return (x + y <= 30) or (y <= x + 2) or (y >= A)

for A in range(1000, 0, -1):
  if all( f(x,y,A) for x in range(1,300) for y in range(1,300)):
    print( A )
    break

