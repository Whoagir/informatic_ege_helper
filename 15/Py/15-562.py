def F(x, y, A):
  return (4*x + y > 115) or (x > 3*y) or (x + 4*y < A)

def valid( A ):
  return all( F(x, y, A) for x in range(300)
                         for y in range(300)  )

for A in range(600, 0, -1):
  if not valid( A ):
    print( A )
    break
