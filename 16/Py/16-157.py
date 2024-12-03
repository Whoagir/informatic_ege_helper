"""
def F0( n ):
  return 0 if n == 0 else \
         F(n//10) + n % 10
"""
def F( n ):
  return sum( map(int, str(n)) )

start, end = 865_432_015, 1_585_342_628
"""
count = 0
prev = F(start)
for n in range(start+1, end+2):
  f = F(n)
  if f < prev: count += 1
  prev = f
print( count )
"""

while start % 10 != 9: start += 1
while end % 10 != 9: end -= 1
print( (end - start) // 10 + 1 )




"""
count = 0
for n in range(start, end+1):
  if F(n) % 7 != 0: count += 1
print( count )

count = 0
while start % 7 != 0:
  if F(start) % 7 != 0: count += 1
  start += 1
while end % 7 != 0:
  if F(end) % 7 != 0: count += 1
  end -= 1

print( count + (end - start) * 5 // 7 )
"""
