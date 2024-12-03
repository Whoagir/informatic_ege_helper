
start, end = 10000, 20000

def valid( x ):
  divs = [5, 11, 17, 19]
  divsX = [ d for d in divs if x % d == 0 ]
  return len(divsX) == 2

count = 0
mi = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    if mi == 0: mi = x

print( count, mi )