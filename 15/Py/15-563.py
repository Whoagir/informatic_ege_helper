def F(x, y, A):
  return ((A < x) or (x**2 - 7*x + 10 > 0)) and ((A >= y) or (y**2 + 7*y + 12 > 0))

def valid( A ):
  return all( F(x, y, A) for x in range(-100,100)
                         for y in range(-100,100)  )

count = 0
for A in range(-100,100):
  if valid( A ):
    count += 1

print( count )