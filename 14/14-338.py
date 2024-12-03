n0 = 5**2026 + 7*5**1013 + 107

def f( x ):
  N = n0 - x
  count5 = count0 = 0
  while N:
    if N % 6 == 5: count5 += 1
    if N % 6 == 0: count0 += 1
    N //= 6
  return count5 - count0

x = 1
while True:
  if f(x) == 28:
    break
  x += 1

print( x )