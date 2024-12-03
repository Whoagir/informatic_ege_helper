def F(x, A):
  return ((x & 84653 != 0) or (x & 51763 != 0)) <= (x & A > 0)

def valid( A ):
  return all( F(x, A) for x in range(100000) )

for A in range(200000):
  if valid( A ):
    print( A )
    break
