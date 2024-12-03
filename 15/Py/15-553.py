def F(x, A):
  return ((x & 673 != 0) or (x & 189 != 0)) <= (x & A > 0)

def valid( A ):
  return all( F(x, A) for x in range(10000) )

for A in range(10000):
  if valid( A ):
    print( A )
    break
