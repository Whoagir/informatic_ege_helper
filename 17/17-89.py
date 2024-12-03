
start, end = 1234567, 7654321

def valid( x ):
  diff = abs( x % 100 - x // 100000)
  return diff > 0 and x % diff == 0

count = 0
ma = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    ma = x

print( count, ma )