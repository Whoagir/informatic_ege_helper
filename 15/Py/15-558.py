def F(x, y, A):
  return (5*x + y > 63) or (x > 2*y) or (3*x + 2*y < A)

def valid( A ):
  return all( F(x, y, A) for x in range(100)
                         for y in range(100)  )

for A in range(500, 0, -1):
  if not valid( A ):
    print( A )
    break
