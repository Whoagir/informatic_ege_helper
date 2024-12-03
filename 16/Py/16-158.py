
"""
def F0( a, b ):
  return 0 if a == 0 and b == 0 else \
         F( a-1, b ) + b if a > b else \
         F( a, b-1 ) + a
def F( a, b ):
  return a*b

for a in range(10):
  for b in range(10):
    print( a, b, F(a, b) )
"""

n = 2744000
count = 0
for d in range(1,n+1):
  if n % d == 0:
    count += 1
    print( d, n // d )

print( count )
