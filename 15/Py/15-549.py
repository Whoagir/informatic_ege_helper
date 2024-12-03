def F(x, A):
  return (x & 3582 == 0) <= ((x & 4531 != 0) <= (x & A != 0))

def valid( A ):
  return all( F(x, A) for x in range(1,5000) )

for A in range(1,5000):
  if valid( A ):
    print( A )
    break
