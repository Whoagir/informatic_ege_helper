
for A in range(500):
  if all( (x + 2*y > A) or (y < x) or (x < 30)
          for x in range(100) for y in range(100)):
    print(A)
