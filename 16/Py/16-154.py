
"""
def F0( n ):
  return 0 if n == 0 else F(n) + 2*n
"""
def F( n ):
  return (2 + 2*n)*n//2

start, end = 100_000_000, 200_000_000
"""
count = 0
for n in range(start, end+1):
  if F(n) % 3 != 0: count += 1
print( count )
"""

while F(start) % 3 != 0: start += 1
while F(end) % 3 != 0: end -= 1

print( (end - start) // 3 + 1 )