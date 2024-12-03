
"""
def F0( n ):
  return 0 if n == 0 else F(n) + 5*n
"""
def F( n ):
  return (5 + 5*n)*n//2

start, end = 189_456_678, 567_654_321

"""
count = 0
for n in range(start, end+1):
  if F(n) % 7 != 0: count += 1
print( count )
"""

#----------------------------------------

count = 0
while start % 7 != 0:
  if F(start) % 7 != 0: count += 1
  start += 1
while end % 7 != 0:
  if F(end) % 7 != 0: count += 1
  end -= 1

print( count + (end - start) * 5 // 7 )

#----------------------------------------

count = 0
for n in range(start, end+1):
  if (n*(n+1)*5//2) % 7 != 0:
    count += 1
print( count )

