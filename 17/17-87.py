
start, end = 25000, 35000

def valid( x ):
  divs = [7, 13, 17, 19]
  divsX = [ d for d in divs if x % d == 0 ]
  return len(divsX) == 2

count = 0
s = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    s += sum( map(int, str(x)) )

print( count, s )