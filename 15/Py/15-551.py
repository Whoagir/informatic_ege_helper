def F(x, A):
  return (x & 73156 == 0) <= ((x & 63567 != 0) <= (x & A != 0))

def valid( A ):
  return all( F(x, A) for x in range(1,80000) )

for A in range(1,80000):
  if valid( A ):
    print( A )
    break
