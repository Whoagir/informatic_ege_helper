def F(x, A):
  return (x & 27358 != 0) <= ((x & 12345 == 0) <= (x & A != 0))

def valid( A ):
  return all( F(x, A) for x in range(1,30000) )

for A in range(1,30000):
  if valid( A ):
    print( A )
    break
