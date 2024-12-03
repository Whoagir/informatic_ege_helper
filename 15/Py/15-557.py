def F(x, A):
  return ((x & 32765 != 0) or (x & 22635 != 0)) <= (x & A > 0)

def valid( A ):
  return all( F(x, A) for x in range(80000) )

for A in range(80000):
  if valid( A ):
    print( A )
    break
