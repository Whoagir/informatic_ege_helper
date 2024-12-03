
start, end = 10, 9999

def valid( x ):
  s = bin(x)[2:]
  return s.count('0') == 5 and x % 2 == 1 and x % 33 == 0

count = 0
ma = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    ma = x

print( count, ma )