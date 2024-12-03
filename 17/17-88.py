
start, end = 54123, 75321

def valid( x ):
  divs = list( range(10, 21) )
  divsX = [ d for d in divs if x % d == 0 ]
  return len(divsX) == 5

count = 0
ma = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    ma = x

print( count, ma )