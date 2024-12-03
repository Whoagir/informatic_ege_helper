
start, end = 23561, 64354

def valid( x ):
  count = 2
  q = round(x**0.5)
  if q*q == x:
    count += 1
    q -= 1
  for i in range(2, q+1):
    if x % i == 0:
      count += 2
  return count > 20

count = 0
mi = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    if mi == 0: mi = x

print( count, mi )