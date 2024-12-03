def f(x, y, A):
  return (x**2 - 11*x + 28 > 0) or (y**2 - 9*y + 14 > 0) or (x**2 + y**2 > A)

for A in range(0,100):
  OK = 1
  for x in range(0,1000):
    for y in range(0,1000):
      if not f(x, y, A):
        OK = 0
        break
    if not OK: break
  if OK:
    print(A)
    #break
