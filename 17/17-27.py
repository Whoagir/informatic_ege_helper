
start, end = 3712, 8432

def valid( x ):
  divs = [13, 14, 15]
  divsX = [ d for d in divs if x % d == 0 ]
  return len(divsX) >= 1 and x % 2 == x % 4

count = 0
mi = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    if mi == 0: mi = x

print( count, mi )