def F(x, A):
  return ((x & 8375 != 0) or (x & 6743 != 0)) <= (x & A > 0)

def valid( A ):
  return all( F(x, A) for x in range(30000) )

for A in range(20000):
  if valid( A ):
    print( A )
    break
