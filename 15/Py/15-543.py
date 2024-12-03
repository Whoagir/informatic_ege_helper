
for A in range(500):
  if all( (x*y < A) or (x < y) or (9 < x)
          for x in range(100) for y in range(100)):
    print(A)
    break
