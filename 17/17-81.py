start, end = 15, 2000000

def valid( x ):
  s = str(x)
  for c in s:
    if s.count(c) > 1: return True
  return False

count = 0
mi = ma = 0
x = start
while x <= end:
  if valid(x):
    count += 1
    if mi == 0: mi = x
    ma = x
  x *= 2

print( count, ma-mi )