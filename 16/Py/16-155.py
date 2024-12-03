
"""
def F0( n ):
  return 0 if n == 0 else F(n) + 3*n
"""
def F( n ):
  return (3 + 3*n)*n//2

start, end = 123_456_789, 213_789_654
"""
count = 0
for n in range(start, end+1):
  if F(n) % 5 != 0: count += 1
print( count )
"""

count = 0
while start % 5 != 0:
  if F(start) % 5 != 0: count += 1
  start += 1
while end % 5 != 0:
  if F(end) % 5 != 0: count += 1
  end -= 1

print( count + (end - start) * 3 // 5 )