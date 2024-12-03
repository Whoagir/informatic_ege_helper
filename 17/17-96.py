
start, end = -999, 999

def valid( x ):
  return abs(x) % 16 == 15 and x % 12 != 0 and x % 13 != 0

count = 0
ma = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    if abs(x) > ma:
      ma = x

print( count, ma )