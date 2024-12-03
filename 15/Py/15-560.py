def F(x, y, A):
  return (3*x + 2*y > 25) or (x > 2*y) or (x + 4*y < A)

def valid( A ):
  return all( F(x, y, A) for x in range(200)
                         for y in range(200)  )

for A in range(500, 0, -1):
  if not valid( A ):
    print( A )
    break
