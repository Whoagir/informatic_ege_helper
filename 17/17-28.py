
start, end = 3439, 7410

def valid( x ):
  divs = [9, 10, 11]
  divsX = [ d for d in divs if x % d == 0 ]
  return len(divsX) >= 1 and x % 2 != x % 6

count = 0
mi = 0
ma = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    if mi == 0: mi = x
    ma = max(ma, x)

print( count, ma )