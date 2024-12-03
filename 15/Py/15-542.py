
for A in range(500):
  if all( (x < A) or (y < A) or (x + 2*y  > 50)
          for x in range(100) for y in range(100)):
    print(A)
    break
