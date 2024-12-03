def F(x, A):
  return (x & 2735 != 0) <= ((x & 1234 == 0) <= (x & A != 0))

def valid( A ):
  return all( F(x, A) for x in range(1,5000) )

for A in range(1,5000):
  if valid( A ):
    print( A )
    break
