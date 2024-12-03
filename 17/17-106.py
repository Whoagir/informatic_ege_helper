
start, end = 12356, 76435

def valid( x ):
  count = 2
  q = round(x**0.5)
  if q*q == x:
    count += 1
    q -= 1
  for i in range(2, q+1):
    if x % i == 0:
      count += 2
  return count > 15

count = 0
ma = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    ma = x

print( count, ma )