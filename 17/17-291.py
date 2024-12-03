def toBase( n, b ):
  s = ''
  if n == 0: return '0'
  while n:
    s = str(n%b) + s
    n //= b
  return s

data = [ int(x) for x in open("17-290.txt") ]
N = len(data)
count, ma = 0, None
for i in range(N-2):
   triple = data[i:i+3]
   if any( x % 5 == 4 for x in triple ) and \
      all( '0' not in toBase(x,6) for x in triple ):
     count += 1
     diff = max(triple) - min(triple)
     if ma == None or diff > ma:
       ma = diff

print( count, ma )
