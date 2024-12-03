
start, end = 1985, 8528

def valid( x ):
  divs = [2, 7, 47]
  divsX = [ d for d in divs if x % d == 0 ]
  return len(divsX) == 0 and x % 10 + (x // 10) % 10 == 6

p = 1
ma = 0
for x in range(start, end+1):
  if valid(x):
    p = (p * x) % 1000
    ma = max(ma, x)

print( ma, p )