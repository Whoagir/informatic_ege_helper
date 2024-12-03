
start, end = 56123, 97354

def valid( x ):
  count = 2
  q = round(x**0.5)
  if q*q == x:
    count += 1
    q -= 1
  for i in range(2, q+1):
    if x % i == 0:
      count += 2
  return count > 35

count = 0
s = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    s += x

print( s )
print( count, int(s/count) )