
start, end = 15000, 25000

def valid( x ):
  divs = [7, 11, 17, 19]
  divsX = [ d for d in divs if x % d == 0 ]
  return len(divsX) == 2

count = 0
ma = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    ma = x

print( count, ma )