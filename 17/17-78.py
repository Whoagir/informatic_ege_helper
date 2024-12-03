start, end = 1082, 129932

def valid( x ):
  s = str(x)
  for i in range(1,len(s)):
    if s[i] >= s[i-1]: return False
  count = 2
  for i in range(2,x-1):
    if x % i == 0:
      count += 1
  return count % 3 == 0

def valid7( x ):
  s = str(x)
  return s[0] == '7'

count = 0
ma = 0
for x in range(start, end+1):
  if valid(x):
    count += 1
    if valid7(x):
      ma = x

print( count, ma )